from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Carousel(models.Model):
    img= models.ImageField()
    name= models.CharField(max_length=200, default="p")
    alt= models.CharField(max_length=250, default="sl")
    des= models.CharField(max_length=255, default="")


class Product(models.Model):
    img_url = models.CharField(max_length=2083, default="")
    price = models.FloatField()
    name= models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('view1', args=(str(self.id)))


class Item(models.Model):
    img_url = models.CharField(max_length=2083, default="")
    price = models.FloatField()
    discount= models.FloatField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True,  null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:view', args=(str(self.id)))

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', args=(str(self.id)))


    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', args=(str(self.id)))


class Staff(models.Model):
    name= models.CharField(max_length=100)
    position= models.CharField(max_length=50)
    img= models.ImageField(default="", upload_to='images/')


class OrderItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

class Order(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date= models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total