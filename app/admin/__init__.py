#!/usr/bin/env python3
# encoding: utf-8

from ..decorators import admin_required
from flask_login import login_required
from flask_admin import Admin, AdminIndexView, expose




class MyHomeView(AdminIndexView):
    @expose('/')
    @login_required
    @admin_required
    def index(self):
        arg1 = 'Hello3214532643264564745876865898796789564532543'
        return self.render('admin/index.html', arg1=arg1)




my_flask_admin = Admin(index_view=MyHomeView(name = 'Home', menu_icon_type='glyph', menu_icon_value='glyphicon-home'), template_mode='bootstrap3')

from . import views, forms
