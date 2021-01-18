from django.urls import path
from product.views import Home, about, contact,  AllProducts, View, staff, brand, AddAll
urlpatterns=[
    path('', Home, name="Home"),
    path('staff/', staff, name="staff"),
    path('about/', about, name="About"),
    path('brand/', brand),

    path('contact/',contact, name="Contact" ),

    path('products/',AllProducts.as_view(), name="products"),
    path('post/', AddAll.as_view(), name="add"),

    path('view/<int:pk>', View.as_view(), name="view"),
]