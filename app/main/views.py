#!/usr/bin/env python3
# encoding: utf-8


from . import main
#from ..email import send_email
#from .forms import NameForm
from ..models import Role, User


from flask import render_template,redirect,url_for
#from flask import session




@main.route('/')
def index():
    user = User.query.filter().first()
    #return " <p>Work as Normal!</p> "
    return render_template('index.html')

@main.route('/contact/')
def contact():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('contact.html')

@main.route('/forgot_password/')
def forgot_password():
    return render_template('forgot_password.html')

@main.route('/sidebar/')
def sidebar():
    return render_template('sidebar.html')

"""
#authenticatioin route
from .. import auth


@auth.route('/login/')
def login():
    return render_template('auth/login.html')
# 这里需要注意，这个模板文件需要保存在auth这个文件夹中
# 但是这个文件夹又需要保存在app/templates中
# flask认为模板的路径是相对于程序模板文件夹而言的。
"""
