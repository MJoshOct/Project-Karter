from django.contrib import admin
from django.urls import path,include
from sell.views import *
#from rent.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/",include("search.urls")),
    path("forum/", include("forum.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("home.urls")),   
    path("profile/", include("profile.urls")),
    path("rent/", include("rent.urls")),
    path("sell/", include("sell.urls")),
    #path("rent/<int:product_id>/", rent_request_view, name="rent_request"),
    #path("rents/", rent_request_view, name="rent_request"),

]

