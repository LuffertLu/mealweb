from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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

if __name__ == '__main__':
	main()