from django.urls import path
from product.views import Home, about, contact,  AllProducts, View, special, brand

urlpatterns=[
    path('', Home.as_view(), name="Home"),
    path('special/', special, name="special"),
    path('about/', about, name="About"),
    path('brand/', brand, ),

    path('contact/',contact, name="Contact" ),
    path('products/',AllProducts.as_view(), name="products"),

    path('view/<int:pk>', View.as_view(), name="view"),
]