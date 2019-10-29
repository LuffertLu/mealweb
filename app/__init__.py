#Internal dependency
from config import config
from .main import main as main_blueprint

#Flask related dependency
from flask import Flask,render_template,request 
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

#Database related dependency
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


#Initialization start
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
#?adb = SQLAlchemy(app)


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
#	mail.init_app(app)
#	moment.init_app(app)
	db.init_app(app)
	app.register_blueprint(main_blueprint)
	return app





