from django.contrib import admin
from .models import Product, Products, PostImage, Tecno

class PostImageAdmin(admin.StackedInline):
    model = PostImage
@admin.register(Product)
class PostImageAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Product

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Products)
admin.site.register(Tecno)
