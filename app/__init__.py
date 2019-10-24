from flask import Flask,render_template,request 
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from app.main import main as main_blueprint
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

app.register_blueprint(main_blueprint)

def create_app():
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)

	return app

