from django.db import models

# Create your models here.
class Destination(models.Model):
    # id : models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    special = models.BooleanField(default=False)

class Packages(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics')
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    special = models.BooleanField(default=False)
