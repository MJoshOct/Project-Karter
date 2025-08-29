from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import UserProfile

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate using username (Django default is username, so we find it by email)
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("profiles:view_profile")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "login_form.html")  # HTML file from your template


def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect("login:signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("login:signup")

        # Create user
        username = email.split("@")[0]  # simple username from email
        user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
        # Create profile
        UserProfile.objects.create(user=user)

        messages.success(request, "Account created! Please login.")
        return redirect("login:login")

    return render(request, "signup_form.html")  # HTML file from your template


def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login:login")
