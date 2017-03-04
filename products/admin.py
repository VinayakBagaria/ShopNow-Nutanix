from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information',{'fields':['category']}),
        ('Product Description',{'fields':['name','description','price','num_left','image']})
    ]

    list_display = ('pk', 'name', 'category', 'price')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Product,ProductAdmin)