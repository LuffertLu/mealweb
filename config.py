#config file
import os
basedir = os.path.abspath(os.path.dirname(__file__))

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
#	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') OR 'mysql:///' + os.path.join(basedir, 'data-dev.mysql')
		


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "mysql://admin:1qaz@localhost/meal_dev"
#	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') OR 'mysql:///' + os.path.join(basedir, 'data-dev.mysql')

		

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = "mysql://admin:1qaz@localhost/meal"
#	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') OR 'mysql:///' + os.path.join(basedir, 'data.mysql')



config = {
         'development' : DevelopmentConfig,
         'testing' : TestingConfig,
         'production' : ProductionConfig,
         'default' : DevelopmentConfig
         }


