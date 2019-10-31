#!/usr/bin/env python3
# encoding: utf-8
#Internal dependency
import os
from app import create_app, db

from app.models import User, Role

#Flask related dependency
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate
from flask_sqlalchemy import SQLAlchemy

#Database related dependency




#Code Start
#app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)
app.secret_key = os.urandom(24)

@app.shell_context_processor
def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	manager.add_command("shell",
						Shell(make_context=make_shell_context))




if __name__=="__main__":
    manager.run()
    
