from django.contrib import admin
from .models import Product, Products, Staff


admin.site.site_header = 'HollyMab Global Enterprises'
admin.site.register(Product)
admin.site.register(Products)
admin.site.register(Staff)