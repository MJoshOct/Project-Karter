from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/",include("search.urls")),
    path("forum/", include("forum.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("home.urls")),   
    path("profile/", include("profile.urls")),
    path("sell/",include("sell.urls"))
]

