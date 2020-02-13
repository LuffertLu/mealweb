#!test Flask_admin
from flask import Flask
from flask_admin import BaseView, expose, Admin, expose_plugview
from flask_admin.model import BaseModelView

class MyHomeView(BaseView):
    @expose('/')
    def index(self):
        return 'Hello World jio!'

class MyModelView(BaseModelView):
    @expose('/myview/')	
    def mymodelview(self):
    	column_list = ('name', 'last_name', 'email')
 

app = Flask(__name__)

admin = Admin(app, name='mealweb', template_mode='bootstrap3')
admin.add_view(MyHomeView(name='My Home View', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))
admin.add_view(MyModelView(name = 'myview', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))

app.run()