#!/usr/bin/env python3
# encoding: utf-8


from . import main
from ..email import send_email
from .forms import NameForm
from ..models import Role, User, Permission
from ..decorators import admin_required, permission_required


from flask import render_template,redirect,url_for, request, session
from flask_login import login_required




@main.route('/')
def index():
    user = User.query.filter().first()
    #return " <p>Work as Normal!</p> "
    return render_template('index.html')

@main.route('/contact/')
def contact():
    n=request.args.get('user')
    return render_template('contact.html')


@main.route('/services/')
def services():
    return render_template('services.html')

@main.route('/about/')
def about():
    return render_template('about.html')

@main.route('/pricing/')
def pricing():
	return render_template('pricing.html')

@main.route('/admin/')
@login_required
@admin_required
def for_admins_only():
	return "For administrators!"
