from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Product(models.Model):
    img = models.FileField(null=True, blank=True, upload_to="images/")
    price = models.FloatField()
    name= models.CharField(max_length=50)


    def get_absolute_url(self):
        return reverse('view1', args=(str(self.id)))


class Products(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.FloatField()
    body = RichTextField(blank=True, null=True)
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('view', args=(str(self.id)))

