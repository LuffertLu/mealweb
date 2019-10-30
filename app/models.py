#Internal dependency
from . import db

#Flask related dependency


#Database related dependency
#from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref




#engine = db.create_engine('mysql://admin:1qaz@localhost/meal_dev')
#Base = db.declarative_base(engine)
#Base.metadata.create_all()


class Role(db.Model):
	__tablename__ = 'role'
	id = Column(Integer, primary_key = True)
	rolename = Column(String(64), unique = True, nullable = False)
	user = relationship('User', backref = 'role', lazy = 'dynamic')

	def __repr__(self):
		return '<Role: %r>' % self.rolename




class User(db.Model):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	username = Column(String(64), unique = True, index = True, nullable = False)
	email = Column(String(64), unique = True)
	role_id = Column(Integer, ForeignKey('role.id'))

	def __repr__(self):
		return '<User: %r>' % self.username




class Plant(db.Model):
	__tablename__ = 'plant'
	id = Column(Integer, primary_key = True)	
	plantname = Column(String(64))
	color = Column(String(64))

	def __repr__(self):
		return '<Plant: %r>' % self.plantname		
