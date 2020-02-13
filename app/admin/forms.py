#!/usr/bin/env python3
# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError, EqualTo
from ..models.account import User, Role
from ..models.meal import Food, Cuisine, Cook, Taste




#Code start
class EditFoodForm(FlaskForm):
	"""docstring for loginForm"""
	id = IntegerField('', validator = DataRequired())
	foodname = StringField('食物')
	submit = SubmitField('登录')

	def validate_id(self, field):
		if User.query.filter_by(email = field.data).first():
			raise ValidationError('Email already regisered.')

	def validate_username(self, field):
		if User.query.filter_by(username = field.data).first():
			raise ValidationError('Username already in use.')

