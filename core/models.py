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
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __rep__(self):
        return '<Customer: {}>'.format(self.name)


# Baskets for Customers
class Basket(models.Model):
    customer = models.OneToOneField(
        Customer, related_name='customer', null=False, blank=False, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return str(self.customer) + "_basket"

    def __rep__(self):
        return '<Basket: {}>'.format(self.customer)


# Items in Customer Basket
class BasketItem(models.Model):
    basket = models.ForeignKey(
        Basket, related_name='basket', null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='product', null=False, blank=False, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return str(self.product)
