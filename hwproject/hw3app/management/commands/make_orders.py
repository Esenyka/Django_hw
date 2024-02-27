from django.core.management.base import BaseCommand
from hw3app.models import Product, Client, Order
import random


class Command(BaseCommand):
    help = "Make order with Client Id and product name"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Product name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        product = Product.objects.filter(name=name).first()
        total_am = product.price
        order = Order(customer=client, total_amount=total_am)
        product.product_quantity = product.product_quantity - 1
        product.save()
        order.save()
        order.products.add(product)