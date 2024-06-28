from django.urls import path
from .views import products, product_create


app_name = 'inventory'

urlpatterns = [
    path('products', products, name='products'),
    path('product_create', product_create, name='product_create'),
]