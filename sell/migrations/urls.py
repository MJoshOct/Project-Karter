
from django.urls import path
#from . import views
from sell.views import *

urlpatterns = [
    path("",sell_product , name="sell_product"),
]


