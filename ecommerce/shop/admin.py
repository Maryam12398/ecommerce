
# Register your models here.
from django.contrib import admin
from .models import Customer_user

@admin.register(Customer_user)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'image')
