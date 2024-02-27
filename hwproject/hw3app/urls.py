from django.urls import path
from .views import base_hw3, client_orders_seven, upload_image, products

urlpatterns = [
    path('', base_hw3),
    path('orders/<int:client_id>/', client_orders_seven),
    path('image/', upload_image),
    path('product/<str:product_name>/', products),
]
