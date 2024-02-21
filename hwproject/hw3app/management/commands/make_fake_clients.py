from django.core.management.base import BaseCommand
from hw3app.models import Client
import random


class Command(BaseCommand):
    help = "Fill DB fake data"

    def handle(self, *args, **kwargs):
        names = ["Petr", "Masha", "Sasha", "Vanya", "Kirill"]
        for i in range(len(names)):
            name = names[i]
            num = str(random.randint(0, 999999999)).zfill(9)
            client = Client(name=name, email=f"{name}@mail.com", phone_number=int(num), address=f"{name}ushkina 48")
            client.save()