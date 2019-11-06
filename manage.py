#!/usr/bin/env python3
# encoding: utf-8
import os

#Create app
from app import create_app, db
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

#create app manager
from flask_script import Manager, Shell
manager = Manager(app)

#init and migrate DB
from flask_migrate import MigrateCommand, Migrate
migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

from app.models import User, Role


@app.shell_context_processor
def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	manager.add_command("shell",
						Shell(make_context=make_shell_context))

app.secret_key = os.urandom(24)


if __name__=="__main__":
    manager.run()
    #app.run(debug = True, port = 8000)
