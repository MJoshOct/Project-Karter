from django.urls import path
from . import views

app_name = "forum" 

urlpatterns = [
    path("", views.question_list, name="question_list"),
    path("question/<slug:slug>/", views.question_detail, name="question_detail"),
    path("ask/", views.ask_question, name="ask_question"),
    path("search/", views.forum_search, name="forum_search"),
    
]
