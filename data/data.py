import os
from dataclasses import dataclass


@dataclass
class Person:
    fullname: str
    first_name: str
    last_name: str
    age: int
    email: str
    current_address: str
    permanent_address: str
    salary: int
    department: str
    phone_number: str


DOWNLOAD_DIR = os.path.join(os.getcwd(), 'downloads')
