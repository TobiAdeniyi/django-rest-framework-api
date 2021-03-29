from django.contrib import admin

# Register your models here.
from .models import Product, Basket, Customer


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketsAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    pass
