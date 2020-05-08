#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, BooleanField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, EqualTo
from ..models.meal import Food, Cuisine, Cook, Taste




#Code start
class IntentionForm(FlaskForm):
	"""docstring for loginForm"""
	storage = StringField('还剩什么食物要做菜？', validators = [DataRequired(), Length(1, 64)])	
	random_all = BooleanField('完全随机选择')
	meat_mandontory = BooleanField('必须要有纯肉菜')
	vegetable_mandontory = BooleanField('必须要有纯素菜')
	fruit_mandantory = BooleanField('要有水果')

	submit = SubmitField('选择这顿的菜谱')




class SuggestionForm(FlaskForm):
	"""docstring for RegistrationFormm"""
	name = StringField('菜名', validators= DataRequired)
	URL = StringField('URL', validators = DataRequired)
	mealtime = DateTimeField('就餐时间', validators = DataRequired)
	main_food = StringField('主料', validators = DataRequired)	
	cook = StringField('工艺', validators = DataRequired)
	taste = StringField('口味', validators = DataRequired)
	user_id = StringField('用户ID', validators = DataRequired)





