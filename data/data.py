from dataclasses import dataclass


@dataclass
class Person:
    fullname: str
    email: str
    current_address: str
    permanent_address: str
