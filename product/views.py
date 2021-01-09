from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Products, Tecno

class Home(ListView):
    model = Product
    template_name = 'index.html'


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def special(request):
    return render(request, 'special.html')



def brand(request):
    return render(request, 'brand.html')

class AllProducts(ListView):
    model = Products
    template_name = 'products.html'


class View(DetailView):
    model = Products
    template_name = 'view.html'
