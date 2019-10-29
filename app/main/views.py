#Internal dependency
from . import main
from .. import db
from ..models import User
from ..email import send_email
from .forms import NameForm

#Flask related dependency
from flask import Blueprint
from flask import render_template,session,redirect,url_for,current_app

#Database related dependency


#already in init file check if needed
#main = Blueprint('main', __name__, url_prefix='')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contact/')
def contact():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('contact.html',Data=dic)

@main.route('/login/')
def login():
    return render_template('login.html')

@main.route('/register/')
def register():
    return render_template('register.html')

@main.route('/forgot-password/')
def forgot-password():
    return render_template('forgot-password.html')

@main.route('/sidebar/')
def sidebar():
    return render_template('sidebar.html')
