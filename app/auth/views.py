#!/usr/bin/env python3
# encoding: utf-8
#Internal dependency
from .. import db
from ..models import Role, User
#from ..email import send_email
from .forms import NameForm
from . import auth

#Flask related dependency
from flask import Blueprint
from flask import render_template,session,redirect,url_for,current_app

#Database related dependency




@auth.route('/login/', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	# 创建一个对象
    # GET请求时，视图函数直接渲染模板显示表单
    # POST请求时，拓展的下面这个函数会验证表单数据
    if form.validate_on_submit():
    	user = User.query.filter_by(email = form.email.data).first()
    	if user is not None and user.verify_password(form.password.data):
    		login_user(user, form.remember_me.data)
    		next = request.args.get('next')
    		if next is None or not next.startswith('/'):
    			next = url_for('main.index')
    		return redirect(next)
    	flash('用户名或者密码无效')
    return render_template('auth/login.html', form = form)
# 这里需要注意，这个模板文件需要保存在auth这个文件夹中
# 但是这个文件夹又需要保存在app/templates中
# flask认为模板的路径是相对于程序模板文件夹而言的。

@auth.route('/logout/')
@login_required
def logout():
    logout_user()  # 这也是flask-login拓展提供的将当前用户登出的方法
    flash('用户登出')
    return redirect(url_for('main.index'))



