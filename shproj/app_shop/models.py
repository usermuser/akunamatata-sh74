from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    #price_in_dollars = models.DecimalField(max_digits=6, decimal_places=2)


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Catalog(models.Model):
    name = models.CharField(max_length=200)
    products=models.ManyToManyField(Product)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name