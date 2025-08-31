from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  # redirect to signup if not logged in
def profile_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        contact_address = request.POST.get("contact_address")
        profile_pic = request.FILES.get("profile_pic")

        profile, created = UserProfile.objects.update_or_create(
            email=email,
            defaults={
                "full_name": full_name,
                "phone_number": phone_number,
                "contact_address": contact_address,
                "profile_pic": profile_pic
            }
        )
        messages.success(request, "Profile saved successfully!") 
        return redirect('profile_view')

    return render(request, "kartprofil.html")
