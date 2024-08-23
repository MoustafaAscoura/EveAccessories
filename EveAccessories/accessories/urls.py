from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('categories', categories, name='categories'),
    path('products', products, name='products'),
    path('product/<int:id>', product, name='product'),
    path('cart', cart, name='cart'),
    path('about', about, name='about')
]
