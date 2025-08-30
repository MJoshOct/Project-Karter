# search/urls.py
from django.urls import path
from blog import views 
from .views import search


urlpatterns = [
    path("", search, name="search_results"),
    path("category/<int:pk>/", views.blog_category, name="blog_category"),
]

