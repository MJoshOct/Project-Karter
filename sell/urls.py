from django.urls import path
from . import views

urlpatterns = [
    path("/sell", views.sell, name="sell"),
    path("sell/success/", views.sell_success, name="sell_success"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"), 
]
