from django.contrib import admin
from .models import *
from products.models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','get_products')

admin.site.register(Cart,CartAdmin)
