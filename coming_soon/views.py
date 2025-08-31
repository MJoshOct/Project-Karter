from django.shortcuts import render

# Create your views here.
# views.py

def coming_soon(request):
    return render(request, "coming_soon.html")
