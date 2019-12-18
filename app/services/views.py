#!/usr/bin/env python3
# encoding: utf-8
from . import services
from .. import main
#from flask_bootstrap import Bootstrap
from flask import render_template, redirect,url_for, flash, request
from .forms import IntentionForm
from ..models.meal import Food, Cuisine, Meal
from .. import db
from .. import bootstrap
from flask_login import login_required, current_user, login_user, logout_user




#Route table
@services.route('/intention/', methods = ['GET', 'POST'])
@login_required
def intention():
    form = IntentionForm()
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
    return render_template('services/intention.html', form = form)
# 这里需要注意，这个模板文件需要保存在auth这个文件夹中
# 但是这个文件夹又需要保存在app/templates中
# flask认为模板的路径是相对于程序模板文件夹而言的。



@services.route('/suggestion/', methods = ['GET', 'POST'])
def suggestion():
    form = SuggestionForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, 
                username = form.username.data,
                password = form.password.data)
        db.session.add(user)
        db.session.commit()
        # 下面我们要生成令牌然后发送邮件
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirmation of Your New Account', 
                    'auth/email/confirm', user = user, token = token)
        flash('we have sent a confirmation email to you, please confirm it!!!')
        return redirect(url_for('main.index'))        
        #flash('Your Account has been registered')
        #return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form = form)

@services.route('/suggestion/<username>/')
@login_required
def suggestion(username):
    user = User.query.filter_by(username=username).first()
    meal = Meal.create_Meal()
    if user is None:
        about(404)
    return render_template('suggestion.html', meal = meal)