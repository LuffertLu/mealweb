#!/usr/bin/env python3
# encoding: utf-8
#Internal dependency


#Flask related dependency
#from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email

#Database related dependency


#Code start
class LoginForm(FlaskForm):
	"""docstring for NameForm"""
	email = StringField('Email', validators = [DataRequired(), Length(1, 64), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('登录')

