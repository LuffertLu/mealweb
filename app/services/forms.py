#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, EqualTo
from ..models.meal import Food, Cuisine, Meal




#Code start
class IntentionForm(FlaskForm):
	"""docstring for loginForm"""
	
	#recent_menu  = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])#list, recent five meals
	#persons
	meat_mandontory = BooleanField('must have meat')
	vegetable_mandontory = BooleanField('must have vegetable')
	fruit_mandantory = BooleanField('must have fruit')

	submit = SubmitField('what do we eat today')


class SuggestionForm(FlaskForm):
	"""docstring for RegistrationFormm"""


	submit = SubmitField('Register Account')



