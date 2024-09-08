from django.contrib import admin
from .models import Category, Product, ProductImage


# Register your models here.
class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
