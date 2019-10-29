from sqlalchemy.orm import sessionmaker
from faker import Faker
from ...app import db

session = sessionmaker(db.engine)()
fake = Faker('zh-cn')

def create_user():
	for i in range(10):
		user = db.User(user name=fake.name(), email=fake.email())
		session.add(user)

def create_role():
	for i in range(10):
		role = db.Role(name=fake.name(), email=fake.email())
		session.add(role)

def create_student():
	for i in range(10):
		student = db.Student(name=fake.name(), email=fake.email())
		session.add(student)

def create_course():
	for i in range(10):
		course = db.Course(name=''.join(fake.words(5)), id=course.id)
		session.add(course)

def main():
	create_users()
	create_roles()
	create_student()
	create_course()
	session.commit()

if __name__ == '__main__':
	main()