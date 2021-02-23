from django.db import models


# Products in Store
class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True)
    color = models.CharField(max_length=100, null=True)
    euler_char = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
