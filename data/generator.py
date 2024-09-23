import datetime
import os
import random
from data.data import Person, Date
from faker import Faker

ru_fake = Faker('ru_RU')
fake = Faker()


def generated_person():
    return Person(
        fullname=ru_fake.name_male(),
        first_name=ru_fake.first_name_male(),
        last_name=ru_fake.last_name_male(),
        age=random.randint(20, 90),
        email=ru_fake.email(),
        salary=random.randint(20000, 300000),
        department=ru_fake.job(),
        current_address=ru_fake.address(),
        permanent_address=ru_fake.address(),
        phone_number=ru_fake.msisdn()
    )


def generated_file():
    """Creates .txt file in the project root directory"""
    file_name = f"test_file_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    return file_path


def generated_date():
    return Date(
        day=fake.day_of_month(),
        month=fake.month_name(),
        year=fake.year(),
        time=fake.time()
    )
