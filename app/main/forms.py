#Internal dependency


#Flask related dependency
from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

#Database related dependency


#Code start
class NameForm(FlaskForm):
	"""docstring for NameForm"""
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

