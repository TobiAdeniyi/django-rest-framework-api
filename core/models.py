from django.db import models
from django.contrib.auth.models import User


# Products in Store
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True)
    color = models.CharField(max_length=100, null=True)
    euler_char = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Customers of the Store
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


# Baskets for Customers
class Basket(models.Model):
    customer = models.ForeignKey(
        Customer, related_name='customer', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return str(self.customer) + "_basket"


# Items in Customer Basket
class BasketItem(models.Model):
    basket = models.ForeignKey(
        Basket, related_name='items', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(
        Product, related_name='+', on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return str(self.basket) + '_' + str(self.product)
