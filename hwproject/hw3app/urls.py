from django.urls import path
from .views import base_hw3, client_orders_seven, \
    upload_image, products, total_quantity_in_view, total_quantity_in_DB

urlpatterns = [
    path('', base_hw3),
    path('orders/<int:client_id>/', client_orders_seven),
    path('image/', upload_image),
    path('product/<str:product_name>/', products),
    path('product/totDB', total_quantity_in_DB),
    path('product/totView', total_quantity_in_view),
]
