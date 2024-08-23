import datetime
import os
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
        permanent_address=fake.address(),
        phone_number=fake.msisdn()
    )


def generated_file():
    """Creates .txt file in the project root directory"""
    file_name = f"test_file_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    return file_path
