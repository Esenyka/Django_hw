from django.core.management.base import BaseCommand
from hw3app.models import Product
import random


class Command(BaseCommand):
    help = "Fill DB fake data"

    def handle(self, *args, **kwargs):
        names = ["Bread", "Butter", "Solt", "Peper", "Milk"]
        for i in range(len(names)):
            product = Product.objects.filter(pk=i+1).first()
            product.delete()