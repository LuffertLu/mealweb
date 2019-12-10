#account model
import hashlib

from datetime import datetime
from .. import db, moment

#Model definition dependency
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime 

from sqlalchemy.orm import relationship, backref, session

#Model definition dependency
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer
from flask import current_app
from .. import login_manager



#User Model start:
class Permission:
	FOLLOW = 1
	COMMENT = 2
	WRITE = 4
	MODERATE = 8
	ADMIN = 16




class Role(db.Model):
	__tablename__ = 'role'
	id = Column(Integer, primary_key = True)
	rolename = Column(String(64), unique = True, nullable = False)
	default = Column(Boolean, default = False, index = True)
	permission = Column(Integer)
	user = relationship('User', backref = 'role', lazy = 'dynamic')

	def __repr__():
		return '<Role %r>' % self.name

	@staticmethod
	def insert_roles():
		role = {
				'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
				'Moderator': [Permission.FOLLOW, Permission.COMMENT,Permission.WRITE, Permission.MODERATE],
				'Administrator': [Permission.FOLLOW, Permission.COMMENT,Permission.WRITE, Permission.MODERATE,Permission.ADMIN],
		}
		default_role = 'User'
		for r in role:
			role = Role.query.filter_by(name=r).first()
			if role is None:
				role = Role(name=r)
			role.reset_permissions()
			for perm in role[r]:
				role.add_permission(perm)
			role.default = (role.rolename == default_role)
			session.add(role)
		session.commit()

	def add_permission(self, perm):
		if not self.has_permission(perm):
			self.permission += perm
		
	def remove_permission(self, perm):
		if self.has_permission(perm):
			self.permission -= perm

	def reset_permissions(self):
		self.permission = 0

	def has_permission(self, perm):
		return self.permission & perm == perm




class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	username = Column(String(64), unique = True, index = True, nullable = False)
	confirmed = Column(Boolean, default = False)
	email = Column(String(64), unique = True)
	__password_hash = Column(String(128))
	role_id = Column(Integer, ForeignKey('role.id'))
	location = Column(String(64))
	about_me = Column(Text())
	member_since = Column(DateTime(), default = datetime.now())
	last_seen = Column(DateTime(), default = datetime.now())

	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)
		if self.role is None:
			if self.email == current_app.config['FLASK_ADMIN']:
				self.role = Role.query.filter_by(name = 'Administrator').first()
			if self.role is None:
				self.role = Role.query.filter_by(default = True).first()

	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute!')

	@password.setter
	def password(self, password):
		self.__password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.__password_hash, password)
		
	def generate_confirmation_token(self, expiration = 3600): # 生成一个令牌，有效期默认一小时
		s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expiration)  #生成具有过期时间的JSON web签名
		return s.dumps({'confirm': self.id}) # 为指定的数据生成一个加密签名，然后生成令牌字符串

	def confirm(self, token):
		s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token) 
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		db.session.add(self)
		db.session.commit()
		return True

	def can(self, perm):
		return self.role is not None and self.role.has_permission(perm)

	def is_administrator(self):
		return self.can(Permission.ADMIN)

	def ping(self):
		self.last_seen = datetime.now
		db.session.add(self)

	def gravatar(self, size = 100, default = 'identicon', rating= 'g'):
		url = 'https://secure.gravatar.com/avatar'
		hash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
		return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash= hash, size= size, default = default, rating = rating)

	def __repr__(self):
		return '<User %r>' % self.username




class AnonymousUser(AnonymousUserMixin):
	def can(self, permission):
		return False

	def is_administrator(self):
		return False
	



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))




login_manager.anonymous_user = AnonymousUser
#User Model End