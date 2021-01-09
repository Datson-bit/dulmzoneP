from django.views.generic import ListView, DetailView

from products.models import Product


class Products(ListView):
    model = Product
    template_name = 'products.html'


class View(DetailView):
    model = Product
    template_name = 'view.html'
