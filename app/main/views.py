#Internal dependency
from .. import db
from ..models import Role, User
#from ..email import send_email
from .forms import NameForm
from . import main
from . import auth

#Flask related dependency
from flask import Blueprint
from flask import render_template,session,redirect,url_for,current_app

#Database related dependency




@main.route('/')
def index():
	#user = User.query.filter().first()
    return render_template('index.html')

@main.route('/contact/')
def contact():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('contact.html')

@auth.route('/login/')
def login():
    return render_template('auth/login.html')
# 这里需要注意，这个模板文件需要保存在auth这个文件夹中
# 但是这个文件夹又需要保存在app/templates中
# flask认为模板的路径是相对于程序模板文件夹而言的。

@main.route('/register/')
def register():
    return render_template('register.html')

@main.route('/forgot_password/')
def forgot_password():
    return render_template('forgot_password.html')

@main.route('/sidebar/')
def sidebar():
    return render_template('sidebar.html')
