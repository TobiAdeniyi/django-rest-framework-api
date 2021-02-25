from django.contrib import admin

# Register your models here.
from .models import Products, Baskets, Customers


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Baskets)
class BasketsAdmin(admin.ModelAdmin):
    pass


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    pass
