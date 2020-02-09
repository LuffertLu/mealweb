#!/usr/bin/env python3
# encoding: utf-8
from . import services
from .. import main
from ..main.requester import requester, get_Cuisine, Show_Cuisine
#from flask_bootstrap import Bootstrap
from flask import render_template, redirect,url_for, flash, request
from .forms import IntentionForm, SuggestionForm
from ..models.meal import Food, Cuisine, Cook, Taste
from ..models.account import Role, User
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
        form.random_all = False
    	#main_food = User.query.filter_by(email = form.email.data).first()
        form.meat_mandontory = False
        form.vegetable_mandontory = False
        form.fruit_mandantory = False
        return redirect(url_for('.suggestion', username = current_user.username, intention = form))
    return render_template('services/intention.html', form = form)





@services.route('/suggestion/<username>', methods = ['GET', 'POST'])
@login_required
def suggestion(username):   
    intention = IntentionForm
    show_cuisine = Show_Cuisine
    show_cuisine_list = []
    if intention.random_all:
        for i in range(5):
            main_food = Food.select_Food_random()
            cook = Cook.select_Cook_random()   
            try:
                show_cuisine = get_Cuisine(main_food, cook)
            except IndexError:
                continue
            if show_cuisine != 'dummy':
                show_cuisine_list.append(show_cuisine)
    else:
        return redirect(url_for('main.index'))
    return render_template('services/suggestion.html', cuisines = show_cuisine_list)
   
    




@services.route('/bom/<username>', methods = ['GET', 'POST'])
@login_required
def bom(username):   
    user = User.query.filter_by(username=username).first()
    cuisine = Cuisine.query.filter_by(id = 1 ).first()
    contents = [i for i in range(5)]
#    meal = Meal.create_Meal()
    if user is None:
        about(404)
 #   form = SuggestionForm()
 #   form.name.data = cuisine.cuisine_name
 #   form.process.data = cuisine.cuisine_process
    return render_template('services/bom.html', contents = contents, cuisine = cuisine)