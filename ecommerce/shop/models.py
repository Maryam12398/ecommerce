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
    warranty = models.CharField(default="no warranty")
    features = models.TextField(blank=True,null=True)
    popular = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product/',default= 'default_png')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    arrival = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    def discounted_price(self):
        return int(self.price - (self.price * self.discount / 100))
    def __str__(self):
        return self.name
  
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    caption = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.product.name} Image"
    
class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specs')
    field = models.CharField(blank=True, max_length=255)  
    value = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.field}"