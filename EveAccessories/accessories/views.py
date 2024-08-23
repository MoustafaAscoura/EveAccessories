from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def categories(request):
    return render(request, 'categories.html')


def products(request):
    return render(request, 'products.html')


def product(request, id):
    return render(request, 'product.html')


def cart(request):
    return render(request, 'cart.html')


def about(request):
    return render(request, 'about.html')
