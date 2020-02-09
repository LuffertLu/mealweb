#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, BooleanField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, EqualTo
from ..models.meal import Food, Cuisine, Cook, Taste




#Code start
class IntentionForm(FlaskForm):
	"""docstring for loginForm"""
	random_all = BooleanField('Random')
	#recent_menu  = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])#list, recent five meals
	#persons
	meat_mandontory = BooleanField('must have meat')
	vegetable_mandontory = BooleanField('must have vegetable')
	fruit_mandantory = BooleanField('must have fruit')

	submit = SubmitField('what do we eat today')


class SuggestionForm(FlaskForm):
	"""docstring for RegistrationFormm"""
	name = StringField('菜名', validators= [Length(0, 64)])
	URL = StringField('URL')
	mealtime = DateTimeField('就餐时间')
	main_food = StringField('主料')	
	cook = StringField('工艺')
	taste = StringField('口味')
	user_id = StringField('用户ID')





