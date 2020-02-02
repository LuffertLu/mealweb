from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from sqlalchemy.orm import sessionmaker
from faker import Faker
from db import engine, User, Course, Lab, Tag

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative imort declarative_base
from ..app.models import Plant, Meat
from sqlalchemy.orm import sessionmaker
from faker import Faker




engine = create_engine("mysql://admin:1qaz@localhost/meal_dev")
Base = declarative_base(engine)
Base.metadata.create_all()

session = sessionmaker(db.engine)()
fake = Faker('zh-cn')

def create_meat():
	for i in range(10):
		meatname = db.Meat(user name=fake.name(), email=fake.email())
		session.add(user)

def create_plant():
	for i in range(10):
		role = db.Role(name=fake.name(), email=fake.email())
		session.add(role)




def main():
	create_meat()
	create_plant()
	session.commit()



session = sessionmaker(engine)()
fake = Faker('zh-cn')

def create_users():
    for i in range(10):
        user = User(name=fake.name(), email=fake.email())
        session.add(user)

def create_courses():
    for user in session.query(User).all():
        for i in range(2):
            course = Course(name=''.join(fake.words(4)), user=user)
            session.add(course)

def create_labs():
    for course in session.query(Course):
        lab = Lab(name=''.join(fake.words(5)), id=course.id)
        session.add(lab)

def create_tags():
    for name in ['python', 'linux', 'java', 'mysql', 'lisp']:
        tag = Tag(name=name)
        session.add(tag)

def main():
    create_users()
    create_courses()
    create_labs()
    create_tags()
    session.commit()

if __name__ == '__main__':
    main()