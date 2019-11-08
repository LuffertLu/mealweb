#!/usr/bin/env python3
# encoding: utf-8
#Internal dependency
from . import db

#Model definition dependency
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from sqlalchemy.orm import relationship, backref

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from itsdangerous import TimedJSONWebSignatureSerializer

from flask import current_app

from . import login_manager





class Role(db.Model):
	__tablename__ = 'role'
	id = Column(Integer, primary_key = True)
	rolename = Column(String(64), unique = True, nullable = False)
	user = relationship('User', backref = 'role', lazy = 'dynamic')





class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	username = Column(String(64), unique = True, index = True, nullable = False)
	confirmed = Column(Boolean, default = False)
	email = Column(String(64), unique = True)
	__password_hash = Column(String(128))
	role_id = Column(Integer, ForeignKey('role.id'))

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

	def __repr__(self):
		return '<User %r>' % self.username
		

class Plant(db.Model):
	__tablename__ = 'plant'
	id = Column(Integer, primary_key = True)	
	plantname = Column(String(64))
	color = Column(String(64))
	



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))