import redis
import hashlib
import json
import copy
from functools import wraps

TTL = 604800
#TTL is one week

class ErrorMessage(Exception):
    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return repr(self.value)

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


def raise_exception(msg_prefix='', *args, **kwargs):
    def deco(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                msg = msg_prefix + str(e)
                raise ErrorMessage(msg)
        return decorated_function
    return deco


class Serializer(object):

    """docstring for Serializer"""

    @staticmethod
    def dumps(data_obj):
        return json.dumps(data_obj)

    @staticmethod
    def loads(data_string):
        return json.loads(data_string)


class Cart(object):

    """
        Main Class for Cart, contains all functionality
    """

    @raise_exception("Cart can't be initialized due to Error: ")
    def __init__(self, user_id, redis_connection, ttl=TTL):
        """
            Constructor for the class, initializes user_id and checks whether
            the users' cart exists or not.
        """
        self.__redis_user_hash_token = "CART"
        self.user_id = user_id
        self.user_redis_key = self.__get_user_redis_key(user_id)
        self.redis_connection = redis_connection
        self.ttl = ttl
        self.user_cart_exists = self.cart_exists(user_id)
        self.destroy = self.__del__

    @raise_exception("ttl can't be set due to Error: ")
    def set_ttl(self, expiry_time=TTL):
        """
            Update the ttl of the cart
        """
        return self.redis_connection.expire(self.user_redis_key, expiry_time)

    @raise_exception("ttl can't be obtained due to Error: ")
    def get_ttl(self):
        ttl = self.redis_connection.ttl(self.user_redis_key)
        if ttl:
            return ttl
        else:
            raise ErrorMessage("User Cart does not exists")

    def __product_dict(self, url, name, extra_data_dict={}):
        """
            Returns the dictionary for a product, with the argument values.
        """
        product_dict = {
            "url": url,
            "name": name
        }
        product_dict.update(extra_data_dict)
        return product_dict

    def __product_id(self, url, name):
        """
            Return the product id to be used in redis
        """
        m = hashlib.md5()
        m.update(bytes(url+name, encoding="utf8"))
        product_id = m.hexdigest()
        return product_id

    @raise_exception("Cart exists can't return a value due to Error: ")
    def cart_exists(self, user_id):
        """
            Confirm user's cart hash in Redis
        """
        return self.redis_connection.exists(self.user_redis_key)

    def __get_user_redis_key_prefix(self):
        """
            Generate the prefix for the user's redis key. 
        """
        return ":".join([self.__redis_user_hash_token, "USER_ID"])

    def __get_user_redis_key(self, user_id):
        """
            Generates the name of the Hash used for storing User cart in Redis
        """
        if user_id:
            return self.__get_user_redis_key_prefix() + ":"+str(user_id)
        else:
            raise ErrorMessage("user_id can't be null")

    @raise_exception("Redis user key can't be obtained due to Error: ")
    def get_user_redis_key(self):
        """
            Returns the name of the Hash used for storing User cart in Redis
        """
        return self.user_redis_key

    @raise_exception("Product can't be added to the User cart due to Error: ")
    def add(self, url, name, **extra_data_dict):
        """
            Returns True if the addition of the product of the given product_id and unit_cost with given quantity 
            is succesful else False.
            Can also add extra details in the form of dictionary.
        """
        product_dict = self.__product_dict(
            url, name, extra_data_dict)
        product_id = self.__product_id(url, name)
        self.redis_connection.hset(
            self.user_redis_key, product_id, Serializer.dumps(product_dict))
        self.user_cart_exists = self.cart_exists(self.user_id)
        self.set_ttl()

    @raise_exception("Product can't be obtained due to Error: ")
    def get_product(self, product_id):
        """
            Returns the cart details as a Dictionary for the given product_id
        """
        if self.user_cart_exists:
            product_string = self.redis_connection.hget(
                self.user_redis_key, product_id)
            if product_string:
                return Serializer.loads(product_string)
            else:
                return {}
        else:
            raise ErrorMessage("The user cart is Empty")

    @raise_exception("contains can't function due to Error: ")
    def contains(self, product_id):
        """
            Checks whether the given product exists in the cart
        """
        return self.redis_connection.hexists(self.user_redis_key, product_id)

    def __get_raw_cart(self):
        return self.redis_connection.hgetall(
            self.user_redis_key)

    @raise_exception("Cart can't be obtained due to Error: ")
    def get(self):
        """
            Returns all the products and their details present in the cart as a dictionary
        """
        return {key: Serializer.loads(value) for key, value in self.__get_raw_cart().iteritems()}

    @raise_exception("count can't be obtained due to Error: ")
    def count(self):
        """
            Returns the number of types of products in the carts
        """
        return self.redis_connection.hlen(self.user_redis_key)

    @raise_exception("remove can't function due to Error: ")
    def remove(self, product_id):
        """
            Removes the product from the cart
        """
        if self.user_cart_exists:
            if self.redis_connection.hdel(self.user_redis_key, product_id):
                self.set_ttl()
                return True
            else:
                return False
        else:
            raise ErrorMessage("The user cart is Empty")

    @raise_exception("Product dictionaries can't be obtained due to Error: ")
    def get_product_dicts(self):
        """
            Returns the list of all product details
        """
        return [Serializer.loads(product_string) for product_string in self.redis_connection.hvals(self.user_redis_key)]

    @raise_exception("copy can't be made due to Error: ")
    def copy(self, target_user_id):
        """
            Copies the cart of the user to the target_user_id
        """
        is_copied = self.redis_connection.hmset(
            self.__get_user_redis_key(target_user_id), self.__get_raw_cart())
        target_cart = Cart(target_user_id)
        target_cart.set_ttl()
        return target_cart if is_copied else None

    def __del__(self):
        """
            Deletes the user's cart
        """
        self.redis_connection.delete(self.user_redis_key)
