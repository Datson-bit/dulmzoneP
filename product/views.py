from django.contrib import messages
from email import message

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Item,OrderItem, Staff, Carousel, Order
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
        carousel= Carousel.objects.all()
        return render(request, 'index.html', {'product': product, 'carousel':carousel })

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
    model = Item
    template_name = 'products.html'


class View(DetailView):
    model = Item
    template_name = 'view.html'


class AddAll(CreateView):
    model = Item
    template_name = 'add_products.html'
    fields = '__all__'


class OrderSummaryView(LoginRequiredMixin, View):
   def get(self, *args, **kwargs):
       try:
           order = Order.objects.get(user=self.request.user, ordered=False)
           context={
               'object':order
           }
           return render(self.request, 'cart.html', context)

       except ObjectDoesNotExist:
           messages.error(self.request,"You do not have an active order" )
           return redirect("/")

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user= request.user,
        ordered=False
    )
    order_qs= Order.objects.filter(user=request.user, ordered=False )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item_id= item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This Item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item was added to your cart.")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This Item was added to your cart.")

    return redirect("view", pk=pk)

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(


        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item_id=item.pk).exists():
            order_item= OrderItem.objects.filter(
                item=item,
                user= request.user,
                ordered=False,
            )[0]

            order.items.remove(order_item)
            messages.info(request, "This Item was removed from your cart your cart.")

        else:
            messages.info(request, "This Item was not in your cart.")
            return redirect("order-summary")
    else:
        messages.info(request, "You do not have an order.")
    return redirect("order-summary")

@login_required
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(


        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item_id=item.pk).exists():
            order_item= OrderItem.objects.filter(
                item=item,
                user= request.user,
                ordered=False,
            )[0]

            if order_item.quantity >1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)

            messages.info(request, "This Item was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item was not in your cart.")
            return redirect("view", pk=pk)
    else:
        messages.info(request, "You do not have an order.")
    return redirect("view", pk=pk)

