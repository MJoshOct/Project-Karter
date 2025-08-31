
from django.urls import path
#from . import views
from rent.views import *

urlpatterns = [
    path("", rent_request_view, name="rent_request_view"),
]


