from django.contrib import admin
from .models import Product, Item,Order, OrderItem, Staff, Carousel


admin.site.site_header = 'HollyMab Global Enterprises'
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Staff)
admin.site.register(Carousel)
admin.site.register(OrderItem)
admin.site.register(Order)