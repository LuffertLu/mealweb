#meal model

import numpy as np
from datetime import datetime
from .. import db

#Model definition dependency
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime 

from sqlalchemy.orm import relationship, backref, session

#Meal Model Start
class YinYangWuXing:
	WUWEI = {'suan':1,'ku':2,'gan':3, 'xin':4, 'xian':5}
	WUSE = {'qing':1, 'chi':2, 'huang':3, 'bai':4, 'hei':5}
	WUXU = {'ji':1, 'yang':2, 'niu':3, 'ma':4, 'zhi':5}
	WUZANG = {'gan':1, 'xin':2, 'pi':3, 'fei':4,'shen':5}
	WUYIN = {'gong'}
	WULEI = {'caomu'}
	WUGU = {'mai':1, 'shu':2, 'ji':3, 'dao':4, 'dou':5}
	WUFANG = {'dong'}
	WUXING = {'chen'}




class Food(db.Model):
	__tablename__ = 'food'
	id = Column(Integer, primary_key = True)
	foodname = Column(String(64))
	species = Column(String(64))
	part = Column(String(64))
	mature_period = Column(Integer, default = 0) #number of mature week
	validweeks = Column(Integer, default =  52) 
	color = Column(String(64))

	def is_matured(self):
		w = datetime.now().isocalendar()[1]-self.validweeks
		if w <=0 :
			w = w+52
		if w >= self.mature_period: #if current week later than matue week
			return True
		else:
			return False




class Cuisine(db.Model):
	__tablename__ = 'cuisine'
	id = Column(Integer, primary_key = True)
	cuisine_name = Column(String(64), nullable = False)
	cuisine_king_id = Column(Integer, ForeignKey('food.id'), nullable = False)
	cuisine_minister_id = Column(Integer, ForeignKey('food.id'), nullable = True)
	cuisine_assist_id = Column(Integer, ForeignKey('food.id'), nullable = True)
	cuisine_envoy_id = Column(Integer, ForeignKey('food.id'), nullable = True)
	cuisine_process = Column(Text(), nullable = False)
	cook_type_id = Column(Integer, ForeignKey('cook.id'), nullable= False)
	cuisine_king = relationship('Food', backref = 'cuisine', foreign_keys = [cuisine_king_id], lazy = 'dynamic')
	cuisine_minister = relationship('Food', backref = 'cuisine', foreign_keys = [cuisine_minister_id], lazy = 'dynamic')
	cuisine_assist = relationship('Food', backref = 'cuisine', foreign_keys = [cuisine_assist_id], lazy = 'dynamic')
	cuisine_envoy = relationship('Food', backref = 'cuisine', foreign_keys = [cuisine_envoy_id], lazy = 'dynamic')

	def select_Cuisine():
		cuisine = Cuisine.query.get(1)
		return cuisine

	def add_Cuisine():
		pass

	def modify_Cuisine():
		pass

	def delete_Cuisine():
		pass


		

class Cook(db.Model):
	"""docstring for Cook"db.Model"""
	__tablename__ = 'cook'
	id = Column(Integer, primary_key = True)
	cooktype = Column(String(64))
	cuisine = relationship('Cuisine', backref = 'cook', lazy = 'dynamic')

	def add_Cook():
		pass




class Meal(db.Model):
	"""docstring for meal""" 
	__tablename__ = 'meal'
	id = Column(Integer, primary_key = True)
	menu = Column(String(128))
	meal_date = Column(DateTime(), default = datetime.now())
	course_id = Column(Integer, ForeignKey('cuisine.id'), nullable = False)
	course = relationship('Cuisine', backref = 'meal', lazy = 'dynamic')

	def create_Meal(*args, **kwargs):
		cuisine = Cuisine
		for x in range(1,10):
			cuisine_list[x]= cuisine.select_Cuisine()

	def create_menu():
		pass

	def select_Meal():
		pass
		
#Meal Model End