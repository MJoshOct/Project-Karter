# blog/urls.py

from django.urls import path
from . import views
from django.http import HttpResponse



urlpatterns = [
    path("", views.blog_index, name="home"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<int:pk>/", views.blog_category, name="blog_category"),
]
