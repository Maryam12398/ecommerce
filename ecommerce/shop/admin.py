
# Register your models here.
from django.contrib import admin
from .models import Customer_user,Product,Category,Brand,ProductImage

@admin.register(Customer_user)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'image')

admin.site.register(Category)
admin.site.register(Brand)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','brand','image','price')
    inlines = [ProductImageInline]
