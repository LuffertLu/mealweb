#!/usr/bin/env python3
# encoding: utf-8
#config file
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	MAIL_SERVER = 'smtp.126.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	#MAIL_USERNAME = os.environ.get('MAIL_USERNAME') it is none at the moment. to be check
	MAIL_USERNAME = 'appdevelopment@126.com'
	#MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') it is none at the moment, to be check
	MAIL_PASSWORD = 'MEAL1QAZ' # 126 mailbox authorized code
	
	FLASK_ADMIN = 'appdevelopment@126.com'
	FLASK_POSTS_PER_PAGE = 15
	FLASK_MAIL_SUBJECT_PREFIX = 'Meal'
	FLASK_MAIL_SENDER = 'kaifa<appdevelopment@126.com>'

	SECRET_KEY = 'meal123'

	@staticmethod
	def init_app(app):
		pass




class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql://admin:1qaz@localhost/meal_dev"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
#	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') OR 'mysql:///' + os.path.join(basedir, 'data-dev.mysql')
		



class TestingConfig(Config):
	TESTING = True
	host = '0.0.0.0'
	port = 80
	SQLALCHEMY_DATABASE_URI = "mysql://admin:1qaz@localhost/meal_dev"
	SQLALCHEMY_TRACK_MODIFICATIONS = True
#	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') OR 'mysql:///' + os.path.join(basedir, 'data-dev.mysql')

		


class ProductionConfig(Config):
	host = '0.0.0.0'
	port = 80
	SQLALCHEMY_DATABASE_URI = "mysql://admin:1qaz@localhost/meal"
	SQLALCHEMY_TRACK_MODIFICATIONS = True
#	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') OR 'mysql:///' + os.path.join(basedir, 'data.mysql')




config = {
         'development' : DevelopmentConfig,
         'testing' : TestingConfig,
         'production' : ProductionConfig,
         'default' : DevelopmentConfig
         }
