from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Product(models.Model):
    img_url = models.CharField(max_length=2083, default="")
    price = models.FloatField()
    name= models.CharField(max_length=50)


    def get_absolute_url(self):
        return reverse('view1', args=(str(self.id)))


class Products(models.Model):
    img_url = models.CharField(max_length=2083, default="")
    price = models.FloatField()
    body = RichTextField(blank=True, null=True)
    name = models.CharField(max_length=50)


    def get_absolute_url(self):
        return reverse('view', args=(str(self.id)))

class Staff(models.Model):
    name= models.CharField(max_length=100)
    position= models.CharField(max_length=50)
    img= models.ImageField(default="", upload_to='images/')