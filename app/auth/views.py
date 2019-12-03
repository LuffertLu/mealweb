#!/usr/bin/env python3
# encoding: utf-8
from . import auth
from .. import main
#from flask_bootstrap import Bootstrap
from flask import render_template, redirect,url_for, flash, request
from .forms import LoginForm, RegistrationForm
from ..models import Role, User
from .. import db
from .. import bootstrap
from ..email import send_email
from flask_login import login_required, current_user, login_user, logout_user


#decoration
@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))



#Route table
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

@auth.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
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

@auth.route('/confirm/<token>/')
@login_required # 这个修饰器会保护这个路由，只有用户打开链接登陆后，才可以执行下面的视图函数
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('you have confirmed your acount and you can login now!')
        return redirect(url_for('auth.login'))
    else:
        flash('The confirmation link is invalid or it has expired')
    return redirect(url_for('main.index'))

@auth.route('/unconfirmed/')
def unconfirmed():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for('main.index'))
	return render_template('auth/unconfirmed.html')

@auth.route('/confirm/')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_email(current_user.email, 'Confrim Your Account', 'auth/email/confirm', user = current_user, token = token)
	flash('A New confirmaiton email has been sent to your mailbox.')
	return redirect(url_for('main.index'))

@auth.route('/forgot_password/')
def forgot_password():
    return render_template('auth/forgot_password.html')