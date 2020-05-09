#!/usr/bin/env python3
# encoding: utf-8


from . import main
from ..email import send_email
from .forms import EditProfileForm
from ..models.account import Role, User, Permission
from ..decorators import admin_required, permission_required
from .. import db

from flask import render_template, redirect, url_for, request, session, flash
from flask_login import login_required, current_user


@main.route('/')
def index():
    user = User.query.filter().first()
    # return " <p>Work as Normal!</p> "
    return render_template('index.html')


@main.route('/contact/')
@login_required
def contact():
    n = request.args.get('user')
    return render_template('contact.html')


@main.route('/services/')
@login_required
def services():
    return redirect(url_for('services.intention'))


@main.route('/about/')
def about():
    return render_template('about.html')


@main.route('/pricing/')
def pricing():
    return render_template('pricing.html')


@main.route('/user/<username>/')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        about(404)
    return render_template('user.html', user=user)


@main.route('/edit-profile/', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        flash("your profile has been updated")
        return redirect(url_for('.user', username=current_user.username))

    form.name.data = current_user.username
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile-admin/', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        flash("your profile has been updated")
        return redirect(url_for('.user', username=current_user.username))

    form.name.data = current_user.username
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile_admin.html', form=form)
