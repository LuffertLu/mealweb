#!/usr/bin/env python3
# encoding: utf-8
from . import services
from .. import main
from ..main.requester import requester
from .cuisine_spider import get_Cuisine, Show_Cuisine
#from flask_bootstrap import Bootstrap
from flask import render_template, redirect,url_for, flash, request
from .forms import IntentionForm, SuggestionForm
from ..models.meal import Food, Cuisine, Cook, Taste
from ..models.account import Role, User
from .. import db
from .. import bootstrap
from flask_login import login_required, current_user, login_user, logout_user
import redis



redis_0 = redis.StrictRedis(host="localhost", port=6379, db=0)  # host和port请根据自己的实际情况写,db默认有15个


@services.before_app_request
def before_request():
    pass




#Route table
@services.route('/intention/')
@login_required
def intention():
    pass
    return render_template('services/intention.html')





@services.route('/suggestion/<rule>', methods = ['GET', 'POST'])
@login_required
def suggestion(rule):
    show_cuisine = Show_Cuisine
    show_cuisine_list = []
    rules = rule.split()
    outputtext = ''
    if rule == 'random': #全随机选
        i = 0
        while i < 5:
            main_food = Food.select_Food_random()
            #main_food = '牛'
            cook = Cook.select_Cook_random() 
            #cook = '炖'
            outputtext = outputtext + main_food + cook + ' '
            try:
                show_cuisine = get_Cuisine(food = main_food, cook = cook)
            except IndexError:
                outputtext=outputtext+'e'
                continue
            if show_cuisine != 'dummy':
                show_cuisine_list.append(show_cuisine)
            else:
                continue
            #show_cuisine_list.append(show_cuisine)
            i = i+1
    else: #有限制条件地选
        i = 1
        outputtext = ''
        while i < len(rules):
            cook = Cook.select_Cook_random()
            outputtext = outputtext + cook
            try:
                show_cuisine = get_Cuisine(food = rules[i], cook = cook)
            except IndexError:
                outputtext = outputtext + 'e'
                continue
            if show_cuisine != 'dummy':
                show_cuisine_list.append(show_cuisine)
            else:
                continue
            i = i+1
    return render_template('services/suggestion.html', cuisines = show_cuisine_list, food = outputtext)
   
@services.route('/foodlist/', methods = ['GET', 'POST'])
@login_required
def foodlist():
    form = IntentionForm()
    rule = 'foodlist'# 创建一个规则字符串对象    
    # GET请求时，视图函数直接渲染模板显示表单    
    # POST请求时，拓展的下面这个函数会验证表单数据
    if form.validate_on_submit():
        rule = rule + ' ' + form.storage.data       
        #rule = rule + form.random_all.data
        #rule = rule + form.meat_mandontory.data
        #rule = rule + form.vegetable_mandontory.data
        #rule = rule + form.fruit_mandantory.data
        return redirect(url_for('.suggestion', rule = rule))
    return render_template('services/foodlist.html', form = form)

@services.route('/mealhistory/', methods = ['GET', 'POST'])
@login_required
def mealhistory():
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
    return render_template('services/mealhistory.html', form = form)

@services.route('/season/', methods = ['GET', 'POST'])
@login_required
def season():
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
    return render_template('services/season.html', form = form)

@services.route('/bom/', methods = ['GET', 'POST'])
@login_required
def bom():   

    return render_template('services/bom.html')