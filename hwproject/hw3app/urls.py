from django.urls import path
from .views import base, hw3, client_orders_seven
urlpatterns = [
    path('', hw3),
    path('orders/<int:client_id>/', client_orders_seven),
]