from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Order, Product
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm

# Create your views here.


def base(requests):
    return render(requests, 'base.html')


def base_hw3(requests):
    return render(requests, 'hw3app/templ_hw3.html')


def hw3(requests):
    return render(requests, "hw3app/templ_about.html")


def client_orders_seven(request, client_id):
    date = datetime.now()
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer_id=client_id).order_by('order_date')
    return render(request, 'hw3app/orders.html', {'client': client,
                                                  'order': orders, 'day': (date.day - 7),
                                                  'month': (date.month - 1), 'year': (date.year - 1)})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            return render(request, 'hw3app/upload_image.html', {'form': form, 'img_obj': image})
    else:
        form = ImageForm()
        return render(request, 'hw3app/upload_image.html', {'form': form})


def products(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'hw3app/products.html', {'product': product})
