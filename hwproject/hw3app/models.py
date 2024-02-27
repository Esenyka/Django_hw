from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Client name: {self.name}, email: {self.email}, ph_num: {self.phone_number}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField(default=0)
    product_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media', default='media/def.jpg')

    def __str__(self):
        return f"{self.name} - {self.description}: costs: {self.price}, product quantity {self.product_quantity}"

    def get_price(self):
        return self.price


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) #удалит все заказы
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} made order: {self.order_date}, total amount = {self.total_amount}"

