from faker import Faker
from models import session,Student
from random import randint

faker = Faker()
students =[]
age = list(range(16,34))

for i in range(10):
    student =Student(
        first_name = faker.first_name(),
        last_name = faker.last_name(),
        age = age[randint(0,14)],
        home_town = faker.street_name()
    )
    students.append(student)
session.bulk_save_objects(students)
session.commit()
