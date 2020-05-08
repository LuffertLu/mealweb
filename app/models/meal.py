#meal model

import numpy as np
from datetime import datetime
from .. import db


#Model definition dependency
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime 

from sqlalchemy.orm import relationship, backref, session
import random

from .account import User

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
	species = Column(String(64), default= 'vegetable')
	mature_week = Column(Integer, default = 0) #number of mature week
	validweeks = Column(Integer, default =  52) 
#	color = Column(String(64), default = 'No')

	def is_matured(self):
		week = datetime.now().isocalendar()[1]-self.validweeks
		if week <=0 :
			week = week+52
		if week >= self.mature_period: #if current week later than matue week
			return True
		else:
			return False
	
	def select_Food_random():
		return Food.query.get(random.randint(1,14)).foodname


		

class Cook(db.Model):
	"""docstring for Cook"db.Model"""
	__tablename__ = 'cook'
	id = Column(Integer, primary_key = True)
	cookname = Column(String(64))

	def select_Cook_random():
		return Cook.query.get(random.randint(1,25)).cookname



class Taste(db.Model):
	"""docstring for Taste"db.Model"""
	__tablename__ = 'taste'
	id = Column(Integer, primary_key = True)
	tastename = Column(String(64))

	def select_Taste_random():
		return Taste.query.get(random.randint(1,5)).tastename




class Cuisine(db.Model):
	__tablename__ = 'cuisine'
	id = Column(Integer, primary_key = True)
	cuisinename = Column(String(64), nullable = False)
	cuisine_url = Column(Text(), nullable = False)
	cuisine_time = Column(DateTime(), default = datetime.now())
	#multiple cuisines to one
	cook_id = Column(Integer, ForeignKey('cook.id'), nullable = False)	
	cuisine_cook = relationship('Cook', backref = 'cuisine', foreign_keys = [cook_id])
	taste_id = Column(Integer, ForeignKey('taste.id'), nullable = False)
	cuisine_taste = relationship('Taste', backref = 'cuisine', foreign_keys = [taste_id])
	food_id = Column(Integer, ForeignKey('food.id'), nullable = False)
	cuisine_food = relationship('Food', backref = 'cuisine', foreign_keys = [food_id])	
	user_id= Column(Integer, ForeignKey('user.id'), nullable = False)
	cuisine_user = relationship('User', foreign_keys = [user_id])

	def select_Cuisine_random():
		#挑选搜索关键字
		#search_url=
		cuisine = Cuisine.query.get(random.randint(1,5))
		return cuisine
				
#Meal Model End