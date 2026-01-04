from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length= 15)
    image = models.ImageField(null=True,blank=True,upload_to='images/',default= 'default_png')
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='brands/')
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    stock = models.BooleanField(default=True)
    popular = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/',default= 'default_png')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    arrival = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    def __str__(self):
        return self.name
    def discount_percentage(self):
        if self.old_price and self.old_price > self.price:
            return int(((self.old_price - self.price) / self.old_price) * 100)
        return 0