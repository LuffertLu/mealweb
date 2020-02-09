#!/usr/bin/env python3
# encoding: utf-8
#basic dependency
from flask import Flask
from config import config 


#Initialization start
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_mail import Mail
mail = Mail()
from flask_moment import Moment
moment = Moment()
from flask_login import LoginManager
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login' # 设置登录页面的端点，路由在蓝本中定义，所以要加上蓝本的名字

from flask_login import current_user, login_required, login_user, logout_user

from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .services import services as services_blueprint




def create_app(config_name):
	app = Flask(__name__)	
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	bootstrap.init_app(app)
	app.register_blueprint(main_blueprint, url_prefix = '')
	db.init_app(app)
	with app.test_request_context():
		db.create_all()	
	mail.init_app(app)
	moment.init_app(app)
	login_manager.init_app(app)

	#please register all modules below
	app.register_blueprint(auth_blueprint, url_prefix = '/auth')
	app.register_blueprint(services_blueprint, url_prefix = '/services')
	# 这里加上了prefix，注册后蓝本中定义的所有路由都会加上这个前缀
 	# 例如所有views中定义的/login会变成/auth/login

	return app



