#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, EqualTo
from ..models import Meat, Plant




#Code start
class IntentionForm(FlaskForm):
	"""docstring for loginForm"""
	 = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('记住我')


	recent_menu #list, recent five meals
	persons
	meat_mandontory = BooleanField('must have meat')
	vegetable_mandontory = BooleanField('must have vegetable')
	fruit_mandantory = BooleanField('must have fruit')

	submit = SubmitField('what do we eat today')


class SuggestionForm(FlaskForm):
	"""docstring for RegistrationFormm"""
	email = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])
	username = StringField('Username', validators = [DataRequired(), Length(1, 64), 
							Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
							'Username mush have only letters, numbers, dots or underscores')])
	password = PasswordField('Password', validators = [DataRequired(), EqualTo('password_c', message = 'Passwords must be same!')])
	password_c = PasswordField('Confirm password', validators = [DataRequired()])

	submit = SubmitField('Register Account')

	def validate_email(self, field):
		if User.query.filter_by(email = field.data).first():
			raise ValidationError('Email already regisered.')

	def validate_username(self, field):
		if User.query.filter_by(username = field.data).first():
			raise ValidationError('Username already in use.')

