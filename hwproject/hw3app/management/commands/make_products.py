from django.core.management.base import BaseCommand
from hw3app.models import Product
import random


class Command(BaseCommand):
    help = "Fill DB fake data"

    def handle(self, *args, **kwargs):
        names = ["Tea", "Coffe", "Juice", "Apple", "Pear"]
        for i in range(len(names)):
            name = names[i]
            num = str(random.randint(10, 100)).zfill(2)
            product = Product(name=name, description=f'This is a {name}', price=float(num),
                              product_quantity=random.randint(0, 15))
            product.save()