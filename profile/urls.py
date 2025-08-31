
from django.contrib import admin
from django.urls import path
#from . import views
from profile.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", profile_view, name="profile_view"),
]


