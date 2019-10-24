from . import db

engine = create_engine('mysql://root@localhost/study?charset=utf8')
Base = declarative_base(engine)
Base.metadata.create_all()


class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True, nullable = False)
	users = db.relationship('User', backref = 'role', lazy = 'dynamic')

	def __repr__(self):
		return '<Role: %r>' % self.name



class User(db.Model):
	"""docstring for User"""
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique = True, index = True, nullable = False)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User: %r>' % self.username



class Student(Base):
	"""docstring for Student"""
	__tablename__ = 'student'
	id = Column(Integer, primary_key = True)
	name = Column(String(64), unique = True, nullable = False)
	email = Column(String(64), unique = True)
	
	def __repr__(self):
		return '<Student: %r>' % self.name



class Course(Base):
	"""docstring for Course"""
	__tablename__ = 'course'
	name = Column(String(64))
	student_id = Column(Integer, ForeignKey('student.id', ondelete = 'CASCADE'))	
	student = relationship('Student', backref = backref('course', cascade = 'all, delete-orphan'))

	def __repr__(self):
		return '<Course: %r>' % self.name		