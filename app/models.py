#!/usr/bin/env python3
# encoding: utf-8
#Internal dependency
from . import db

#Flask related dependency
from werkzeug.security import generate_password_hash, check_password_hash

#Database related dependency
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin



class Role(db.Model):
	__tablename__ = 'role'
	id = Column(Integer, primary_key = True)
	rolename = Column(String(64), unique = True, nullable = False)
	user = relationship('User', backref = 'role', lazy = 'dynamic')

	def __repr__(self):
		return '<Role: %r>' % self.rolename




class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	username = Column(String(64), unique = True, index = True, nullable = False)
	email = Column(String(64), unique = True)
	__password_hash = Column(String(128))
	role_id = Column(Integer, ForeignKey('role.id'))

	def set_password(self, password):
		self.__password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.__password_hash, password)
		
	def __repr__(self):
		return '<User: %r>' % self.username


		

class Plant(db.Model):
	__tablename__ = 'plant'
	id = Column(Integer, primary_key = True)	
	plantname = Column(String(64))
	color = Column(String(64))

	def __repr__(self):
		return '<Plant: %r>' % self.plantname		



@login_mamager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))