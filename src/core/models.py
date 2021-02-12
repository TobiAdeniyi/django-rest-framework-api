from django.db import models


# Store Products
class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True)
    color = models.CharField(null=True)
    euler_char = models.IntegerField(null=True)

    def __str__(self):
        return self.name
