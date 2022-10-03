from django.db import models

# Create your models here.

class Dealer(models.Model):
    
    make = models.CharField(max_length=30)
    modeltype = models.CharField(max_length=100)
    year = models.IntegerField()
    new = models.CharField(max_length=30)
    used = models.CharField(max_length=30)
    finaced = models.CharField(max_length=30)
    cash = models.CharField(max_length=30)


    def __str__(self):
        return self.make 
