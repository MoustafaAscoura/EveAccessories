from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('products', products, name='products'),
    path('product/<int:pk>', product, name='product'),
    path('cart', cart, name='cart'),
    path('about', about, name='about')
]
