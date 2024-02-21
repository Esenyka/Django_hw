from django.core.management.base import BaseCommand
from hw3app.models import Product, Client, Order
import random


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            client = Client.objects.filter(pk=i).first()

            for j in range(4):
                pk = random.randint(6, 11)
                product = Product.objects.filter(pk=pk).first()
                total_am = product.price
                order = Order(customer=client, total_amount=total_am)
                order.save()
                order.products.add(product)