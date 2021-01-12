from django.urls import path
from product.views import Home, about, contact,successView,  AllProducts, View, special, brand, contactf

urlpatterns=[
    path('', Home.as_view(), name="Home"),
    path('special/', special, name="special"),
    path('about/', about, name="About"),
    path('contactf/', contactf, name="email"),
    path('success/', successView, name="success"),

    path('brand/', brand, ),

    path('contact/',contact, name="Contact" ),
    path('products/',AllProducts.as_view(), name="products"),

    path('view/<int:pk>', View.as_view(), name="view"),
]