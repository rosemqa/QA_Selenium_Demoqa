import random
from data.data import Person
from faker import Faker


fake = Faker('ru_RU')


def generated_person():
    return Person(
        fullname=fake.name_male(),
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        age=random.randint(20, 90),
        email=fake.email(),
        salary=random.randint(20000, 300000),
        department=fake.job(),
        current_address=fake.address(),
        permanent_address=fake.address()
    )
