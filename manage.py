#!/usr/bin/env python3
# encoding: utf-8
import os

#Create app
from config import config
from app import create_app, bootstrap, db, mail, moment, login_manager
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand, Migrate
from app.models.account import User, Role
from app.models.meal import Food, Cook, Taste, Cuisine
from app.models.resource import File, Image, Page

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.secret_key = os.urandom(24)

#create app manager
manager = Manager(app)

#init and migrate DB
migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

#init server
server = Server(host=app.config['HOST'], port=app.config['PORT'])
manager.add_command("runserver", server)



@app.shell_context_processor
def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	manager.add_command("shell",
						Shell(make_context=make_shell_context))



if __name__=="__main__":
	manager.run()
    #app.run(debug = True, port = 8000)
