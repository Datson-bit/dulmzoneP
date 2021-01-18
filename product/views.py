from email import message

from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Products, Staff
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings

def Home(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(message_name, message, message_email, ['dulmzonecoders@gmail.com'])
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        product = Product.objects.all()
        return render(request, 'index.html', {'product': product})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(message_name, message, message_email,['dulmzonecoders@gmail.com'])
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html')


def staff(request):
    employee = Staff.objects.all()
    context = {'employees':employee}
    return render(request, 'staff.html', context)


def brand(request):
    return render(request, 'brand.html', )


class AllProducts(ListView):
    model = Products
    template_name = 'products.html'


class View(DetailView):
    model = Products
    template_name = 'view.html'


class AddAll(CreateView):
    model = Products
    template_name = 'add_products.html'
    fields = '__all__'

