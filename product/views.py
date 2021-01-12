from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import ContactForm
from .models import Product, Products
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


class Home(ListView):
    model = Product
    template_name = 'index.html'


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def special(request):
    return render(request, 'special.html')


def contactf(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject= form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['dulmzone@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('success')
    return render(request,'email.html', {'form':form})


def successView(request):
    return HttpResponse('Success! Thank you for your message')


def brand(request):
    return render(request, 'brand.html', )


class AllProducts(ListView):
    model = Products
    template_name = 'products.html'


class View(DetailView):
    model = Products
    template_name = 'view.html'
