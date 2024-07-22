from data.data import Person
from faker import Faker


fake = Faker('ru_RU')


def generated_person():
    return Person(
        fullname=fake.name_male(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address()
    )
