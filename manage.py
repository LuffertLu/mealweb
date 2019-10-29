#Internal dependency
import os
from app import create_app,db
from app.models import User,Role

#Flask related dependency
from flask.ext.script import Manager,Shell
from flask.ext.migrate import  MigrateCommand

#Database related dependency




#Code Start
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	manager.add_command("shell",
						Shell(make_context=make_shell_context))
	manager.add_command('db','MigrateCommand')


if __name__=="__main__":
    manager.run(debug=True, port=9000)
    
