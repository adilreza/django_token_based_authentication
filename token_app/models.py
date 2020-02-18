from django.db import models

# Create your models here.

class RestModel(models.Model):
    data1 = models.CharField(max_length=200)
    data2 = models.CharField(max_length=200)
    data3 = models.CharField(max_length=200)


class RestModel2(models.Model):
    data1 = models.CharField(max_length=200, name="thisName")
    data2 = models.CharField(max_length=200)
    data3 = models.CharField(max_length=200)
    def __str__(self):
        return self.data2
