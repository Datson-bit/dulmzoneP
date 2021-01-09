from django.urls import path
from .views import Products, View
urlpatterns=[
    path('', Products.as_view(), name="products"),
    path('view/<int:pk>', View.as_view(), name="view")
]