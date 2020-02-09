import random
import time

import requests
from requests.exceptions import TooManyRedirects
from lxml import etree
import re

SESSION = requests.Session()
SESSION.max_redirects = 3

def requester(
        url,
        main_url=None,
        delay=0,
        cook=None,
        headers=None,
        timeout=10,
        host=None,
        user_agents=[None],
        failed=None,
    ):
    """Handle the requests and return the response body."""

    # Pause/sleep the program for specified time
    time.sleep(delay)

    def make_request(url):
        """Default request"""
        final_headers = headers or {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#            'Origin': 'https://codebeautify.org',
            'Connection': 'close',
        }
        try:
            response = SESSION.get(
                url,
                cookies=cook,
                headers=final_headers,
                verify=False,
                timeout=timeout,
                stream=True,
            )
        except TooManyRedirects:
            return 'dummy'

        if 'text/html' in response.headers['content-type'] or \
           'text/plain' in response.headers['content-type']:
            if response.status_code != '404':
                return response
            else:
                response.close()
                return 'dummy'
        else:
            response.close()
            return 'dummy'
    
    return make_request(url)



class CuisineCollection:
    def __init__(self, food, cook, cuisine_elements, materiallist, steplist):
        self.food = food
        self.cook = cook
        self.cuisine_elements = []
        self.materiallist = []
        self.steplist = []

    @property
    def parts(self):
        parts = ''
        for part in self.available_parts:
            p = part.xpath('./a/text()')[0]
            parts = parts+p+' '
        return parts.split()

class Show_Cuisine(object):
    """docstring for Show_Cuisine"""
    def __init__(self, target_cuisine):
        self.target_cuisine = target_cuisine
        self.cuisine_url = self.target_cuisine
        self.cuisine_elements = []
        #cuisinename = ""
        #cuisine_img = ""
        #cuisine_taste = ""
        #cuisine_cook = ""
        self.materiallist =[]        
        self.steplist = []

    def add_element(self, cuisinename, cuisine_img, cuisine_taste,cuisine_cook):
        self.cuisine_elements.append([cuisinename, cuisine_img, cuisine_taste, cuisine_cook])

    def add_material(self, food, quantity):
        self.materiallist.append([food, quantity])

    def add_step(self, step_index, step_word):#, step_img_url
        self.steplist.append([step_index, step_word])

def get_Cuisine(food, cook):
    #search_url = 'https://home.meishichina.com/search/'+key_word+'/'
    search_url = 'https://home.meishichina.com/search/'+food+' '+cook+'/'
    root = etree.HTML(requester(search_url).content)
    try:
        s = root.xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/span/text()')[0]
    except IndexError:
        return 'dummy'
    available_cuisines = re.findall(r'\d+', s)    
    if int(available_cuisines[0]) <= 20:
       candidate = int(available_cuisines[0])
    else:       
       candidate = 20 
    target_cuisine_url = root.xpath('/html/body/div[3]/div/div[1]/div[2]/ul/li[{}]/div[2]/h4/a/@href'.format(random.randint(2,candidate)))[0]
    cuisine_process = Show_Cuisine(target_cuisine_url)
    cuisine_root = etree.HTML(requester(cuisine_process.cuisine_url).content)
    #菜名
    cuisinename = cuisine_root.xpath('//*[@id="recipe_title"]/text()')[0]
    #图片URL
    cuisine_img = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[1]/a/img/@src')[0]
    #[口味]&#[工艺]
    cook_tastes = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeCategory_sub_R mt30 clear"]')
    for ct in cook_tastes:
        #[口味]
        cuisine_taste = ct.xpath('./ul/li[1]/span[1]/a/text()')[0]
        #[工艺]
        cuisine_cook = ct.xpath('./ul/li[2]/span[1]/a/text()')[0]
    cuisine_process.add_element(cuisinename, cuisine_img, cuisine_taste, cuisine_cook)
    #材料清单
    #materiallist = []
    items = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/fieldset[@class="particulars"]')
    for item in items:
        categories = item.xpath('./div/ul/li')
        for material in categories:
            try:
                food = material.xpath('./span[1]/a/b/text()')[0]
                quantity = material.xpath('./span[2]/text()')[0]
            except IndexError:
                food = material.xpath('./span[1]/b/text()')[0]
                quantity = material.xpath('./span[2]/text()')[0]
            cuisine_process.add_material(food, quantity)
    #步骤清单
    #steplist = []
    steps = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeStep"]')
    for step in steps:
        details = step.xpath('./ul/li')
        for detail in details:
            try:
                step_index = detail.xpath('./div[2]/div/text()')[0],
                step_word = detail.xpath('./div[2]/text()')[0]
                #step_img_url = detial.xpath('./div[1]/img/@src')[0]
            except IndexError:
                return 'dummy'
            cuisine_process.add_step(step_index, step_word)
    return cuisine_process