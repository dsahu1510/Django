from .models import *
from faker import Faker
fake = Faker()
import random


def generate_random_data(n = 10)->bool:
    [Student.objects.create(
        name = fake.name(),
        age = random.randint(18, 50),
        address = fake.address(),
        fathers_name = fake.name()

    ) for i in range(0, n)]

    return True