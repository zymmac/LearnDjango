import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learn_django.settings')

import django
django.setup()

from faker import Faker
import random
from main_app.models import Shiba

f = Faker('de_DE')
color_list = ['black and tan', 'cream', 'red', 'sesame']
def populate(n=10):
    for i in range(n):
        fake_name = f.first_name()
        fake_color = color_list[random.randint(0,3)]
        fake_birthday = f.date()

        new_shiba = Shiba.objects.get_or_create(name=fake_name, color = fake_color, birthday = fake_birthday)[0]


if __name__ == "__main__":
    print("Generating fake shibas...")
    populate(10)
    print("10 news shibas created!")
