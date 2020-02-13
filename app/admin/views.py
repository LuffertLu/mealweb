#!/usr/bin/env python3
# encoding: utf-8
from . import my_flask_admin

import os
import os.path as op
from redis import Redis
from jinja2 import Markup

#from .. import auth
#from .. import main
from .. import db
from ..decorators import admin_required, permission_required

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user

from flask_admin import expose, contrib, BaseView, form
from flask_admin.form import rules
from flask_admin.contrib import sqla, rediscli
from flask_admin.contrib.sqla import filters
from flask_admin.contrib.sqla.filters import BaseSQLAFilter, FilterEqual

from .forms import EditFoodForm

from ..models.account import Role, User
from ..models.meal import Food, Taste, Cook, Cuisine
from ..models.resource import File, Image, Page, CKTextAreaWidget, CKTextAreaField, file_path

#menu_icon_type='glyph', menu_icon_value='glyphicon-home',


# Customized User model admin
def phone_number_formatter(view, context, model, name):
    return Markup("<nobr>{}</nobr>".format(model.phone_number)) if model.phone_number else None


def is_numberic_validator(form, field):
    if field.data and not field.data.isdigit():
        raise validators.ValidationError(gettext('Only numbers are allowed.'))




class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return current_user.is_authenticated & current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        if not current_user.is_administrator():
            return redirect(url_for('admin.index'))
        else:
        # redirect to login page if user doesn't have access
            return redirect(url_for('auth.login'))



# Administrative views
class AdminView(BaseView):
    @login_required
    @admin_required
    @expose('/')
    def index(self):
        return self.render('admin/myadmin.html')



class AnotherAdminView(BaseView):
    @login_required
    @admin_required
    @expose('/')
    def index(self):
        return self.render('admin/anotheradmin.html')

    @expose('/test4/')
    def test(self):
        return self.render('admin/test.html')

class RoleView(MyModelView):
#id, rolename, default, permission, user
    can_view_details = True  # show a modal dialog with records details

    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'id',
        'rolename',
        'default',
        'permission'
    ]
    
    column_auto_select_related = True





class UserView(MyModelView):
#id, username, confirmed, email, __password_hash, role_id, location, about_me, member_since, last_seen
    can_view_details = True  # show a modal dialog with records details

    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'id',
        'role_id',
        'username',
        'confirmed',
        'email',
        'location',
        'about_me',
        'member_since',
        'last_seen'
    ]

    column_auto_select_related = True  
    
    column_searchable_list = [
        'id',
        'role_id',
        'username',
        'confirmed',
        'email',
        'location',
        'about_me',
        'member_since',
        'last_seen'
    ]

    column_editable_list = [
        'username',
        'confirmed',
        'email',
        'location',
        'about_me',
        'member_since',
    ]


    column_default_sort = [('username', False), ('last_seen', False)]  # sort on multiple columns

    # custom filter: each filter in the list is a filter operation (equals, not equals, etc)

    # filters with the same name will appear as operations under the same filter
    column_filters = [
        'username',
        FilterEqual(column=User.username, name='User Name'),
        #FilterLastNameBrown(column=User.last_name, name='Last Name',
        #                    options=(('1', 'Yes'), ('0', 'No'))),
        'member_since',
        'email',
        'confirmed',
        'last_seen',
        'location',
    ]
#    column_formatters = {'phone_number': phone_number_formatter}

    # setup edit forms so that only posts created by this user can be selected as 'featured'
    form_create_rules = [
        # Header and four fields. Email field will go above phone field.
        
        rules.FieldSet(('username', 'email', 'role','confirmed','member_since','last_seen'), 'Personal'),
        # Separate header and few fields
        rules.Header('Location'),
        rules.Field('location'),
        # String is resolved to form field, so there's no need to explicitly use `rules.Field`
        # Show macro that's included in the templates
        rules.Container('rule_demo.wrap', rules.Field('about_me'))
    ]

    form_edit_rules = form_create_rules

    create_template = 'admin/create_user.html'
    edit_template = 'admin/edit_user.html'





    def edit_form(self, obj):
        return self._filtered_roles(
            super(UserView, self).edit_form(obj)
        )

    def _filtered_roles(self, form):
        form.role.query_factory = lambda: Role.query.filter(Role.permission == form._obj.id).all()
        return form




class FoodView(MyModelView):
#'id',foodname','species','validweeks','mature_week'
    can_view_details = True  # show a modal dialog with records details

    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'id',
        'foodname',
        'species',
        'validweeks',
        'mature_week'
    ]
    
    column_auto_select_related = True




class CookView(MyModelView):
#'id',cookname'
    can_view_details = True  # show a modal dialog with records details

    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'id',
        'cookname'
    ]
    
    column_auto_select_related = True




class TasteView(MyModelView):
#'id',tastename'
    can_view_details = True  # show a modal dialog with records details

    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'id',
        'tastename'
    ]
    
    column_auto_select_related = True




class CuisineView(MyModelView):
#'id','cuisinename','cuisine_url','cuisine_time','cook_id','taste_id','food_id','user_id'
    can_view_details = True  # show a modal dialog with records details

    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'id',
        'cuisinename',
        'cuisine_url',
        'cuisine_time',
        'cook_id',
        'taste_id',
        'food_id',
        'user_id'
    ]
    
    column_auto_select_related = True




class PageView(MyModelView):

    form_overrides = {
        'text': CKTextAreaField
    }
    create_template = 'admin/create_page.html'
    edit_template = 'admin/edit_page.html'





class FileView(MyModelView):

    # Override form field to use Flask-Admin FileUploadField
    form_overrides = {
        'path': form.FileUploadField
    }

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'path': {
            'label': 'File',
            'base_path': file_path,
            'allow_overwrite': False
        }
    }




class ImageView(MyModelView):
    @login_required
    @admin_required
#    @expose('/')
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }





# Create admin interface
#my_flask_admin.add_view(AdminView(name = 'view1'))
#my_flask_admin.add_view(AnotherAdminView(name="view2", category='Test3'))
my_flask_admin.add_view(RoleView(Role, db.session))
my_flask_admin.add_view(UserView(User, db.session))

my_flask_admin.add_view(FoodView(Food, db.session))
my_flask_admin.add_view(CookView(Cook, db.session))
my_flask_admin.add_view(TasteView(Taste, db.session))
my_flask_admin.add_view(CuisineView(Cuisine, db.session))

my_flask_admin.add_view(FileView(File, db.session))
my_flask_admin.add_view(ImageView(Image, db.session))
my_flask_admin.add_view(PageView(Page, db.session))
my_flask_admin.add_view(rediscli.RedisCli(Redis()))