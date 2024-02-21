from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Order
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

# Create your views here.


def base(requests):
    return render(requests, 'hw3app/about.html')


def hw3(requests):
    return render(requests, "hw3app/templ_about.html")


def client_orders_seven(request, client_id):
    date = datetime.now()
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer_id=client_id).order_by('order_date')
    return render(request, 'hw3app/orders.html', {'client': client,
                                                  'order': orders, 'day': (date.day - 7),
                                                  'month': (date.month - 1), 'year': (date.year - 1)})





