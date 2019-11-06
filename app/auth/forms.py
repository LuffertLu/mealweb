#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp





#Code start
class LoginForm(FlaskForm):
	"""docstring for loginForm"""
	email = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
	"""docstring for RegistrationFormm"""
	email = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])
	username = StringField('Username', validators = [DataRequired(), Length(1, 64), 
							Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
							'Username mush have only letters, numbers, dots or underscores')])
	password = PasswordField('Confirm password', validators = [DataRequired()])
	submit = SubmitField('Register Account')

	def validate_email(self, field):
		if User.query.filter_fy(email = field.data).first():
			raise ValidationError('Email already regisered.')

	def validate_username(self, field):
		if User.query.filter_fy(username = field.data).first():
			raise ValidationError('Username already in use.')
		
	def __init__(self, arg):
		super(RegistrationForm, self).__init__()
		self.arg = arg
		