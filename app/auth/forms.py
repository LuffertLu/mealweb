#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError, EqualTo
from ..models.account import User, Role

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
	password = PasswordField('Password', validators = [DataRequired(), EqualTo('password_c', message = 'Passwords must be same!')])
	password_c = PasswordField('Confirm password', validators = [DataRequired()])

	submit = SubmitField('Register Account')

	def validate_email(self, field):
		if User.query.filter_by(email = field.data).first():
			raise ValidationError('Email already regisered.')

	def validate_username(self, field):
		if User.query.filter_by(username = field.data).first():
			raise ValidationError('Username already in use.')



class Forgot_passwordForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Length(1,64), Email()])
	submit = SubmitField('忘记密码')




class New_passwordForm(FlaskForm):
	password = PasswordField('Password', validators = [DataRequired(), EqualTo('password_c', message = 'Passwords must be same!')])
	password_c = PasswordField('Confirm password', validators = [DataRequired()])
	submit = SubmitField('确认修改密码')
