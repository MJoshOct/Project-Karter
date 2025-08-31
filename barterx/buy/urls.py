from django.urls import path
from buy.views import *

urlpatterns = [
    path("<int:product_id>/", buy_page, name="buy"),
]
