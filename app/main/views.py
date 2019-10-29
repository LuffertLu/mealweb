#Internal dependency
#from .. import db
#from ..models import User
#from ..email import send_email
from .forms import NameForm
from . import main

#Flask related dependency
from flask import Blueprint
from flask import render_template,session,redirect,url_for,current_app

#Database related dependency




@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contact/')
def contact():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('contact.html')

@main.route('/login/')
def login():
    return render_template('login.html')

@main.route('/register/')
def register():
    return render_template('register.html')

@main.route('/forgot_password/')
def forgot_password():
    return render_template('forgot_password.html')

@main.route('/sidebar/')
def sidebar():
    return render_template('sidebar.html')
