# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('coming-soon/', views.coming_soon, name='coming_soon'),
]
