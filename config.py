#!/usr/bin/env python3
# encoding: utf-8
#config file

import os
basedir = os.path.abspath(os.path.dirname(__file__))


#SECRET_KEY = 'secret'

class Config:
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME') #it is none at the moment. to be check
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') #it is none at the moment, to be check

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



