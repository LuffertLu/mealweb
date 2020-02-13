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
	meat_mandontory = BooleanField('must have meat')
	vegetable_mandontory = BooleanField('must have vegetable')
	fruit_mandantory = BooleanField('must have fruit')

	submit = SubmitField('what do we eat today')




class SuggestionForm(FlaskForm):
	"""docstring for RegistrationFormm"""
	name = StringField('菜名', validators= DataRequired)
	URL = StringField('URL', validators = DataRequired)
	mealtime = DateTimeField('就餐时间', validators = DataRequired)
	main_food = StringField('主料', validators = DataRequired)	
	cook = StringField('工艺', validators = DataRequired)
	taste = StringField('口味', validators = DataRequired)
	user_id = StringField('用户ID', validators = DataRequired)





