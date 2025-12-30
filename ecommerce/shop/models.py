from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length= 15)
    image = models.ImageField(null=True,blank=True,upload_to='images/',default= 'default_png')
    def __str__(self):
        return self.user.username

class Cetagory(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=15)
    cetagory = models.ForeignKey(Cetagory, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.IntegerField()
    dicount = models.IntegerField()
    def __str__(self):
        return self.name