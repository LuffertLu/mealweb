#!/usr/bin/env python3
# encoding: utf-8
#Internal dependency
from config import config
from .main import main as main_blueprint
from .auth import auth as auth_blueprint


#Flask related dependency
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
#from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

#Database related dependency


#Initialization start
bootstrap = Bootstrap()
moment = Moment()
#mail = Mail()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login' # 设置登录页面的端点，路由在蓝本中定义，所以要加上蓝本的名字



def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	#mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	with app.test_request_context():
		db.create_all()
	login_manager.init_app(app)
	app.register_blueprint(main_blueprint, url_prefix = '')
	app.register_blueprint(auth_blueprint, url_prefix = '/auth')
    # 这里加上了prefix，注册后蓝本中定义的所有路由都会加上这个前缀
    # 所有views中定义的/login会变成/auth/login
	return app






