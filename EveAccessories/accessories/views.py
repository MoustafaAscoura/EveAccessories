from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product


# Create your views here.
def index(request):
    top_categories = Category.objects.all()[:4]
    new_products = Product.objects.order_by("updated_at")[:12]
    return render(request, 'index.html', context={"categories": top_categories, "products": new_products})


class CategoriesView(ListView):
    template_name = "categories.html"
    model = Category
    context_object_name = "categories"


def products(request):
    category = request.GET.get("category", "")
    page = request.GET.get("page")
    return render(request, 'products.html', context={"category": category})


def product(request, pk):
    return render(request, 'product.html')


def cart(request):
    return render(request, 'cart.html')


def about(request):
    return render(request, 'about.html')
