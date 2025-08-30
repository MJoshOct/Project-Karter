from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import UserProfile

def profile_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        contact_address = request.POST.get("contact_address")
        profile_pic = request.FILES.get("profile_pic")   # file upload

        # Save or update user profile
        profile, created = UserProfile.objects.update_or_create(
            email=email,
            defaults={
                "full_name": full_name,
                "phone_number": phone_number,
                "contact_address": contact_address,
                "profile_pic": profile_pic
            }
        )
        return HttpResponse("Profile saved successfully!")

    return render(request, "kartprofil.html")
