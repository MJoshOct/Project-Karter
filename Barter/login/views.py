from django.shortcuts import render

from .models import*

# Create your views here.
def logsign(request):
    if request.method== "POST":
        data = request.POST#brin all data from html website page using this method
        
        email=data.get('email')
        password=data.get('password')
    return render(request,'kartrlogin.html')

def accCreate(request):
    if request.method== "POST":
        data = request.POST#brin all data from html website page using this method
        fullname=data.get('fullname')
        email=data.get('email')
        password=data.get('password')
    return render(request,'kartprofil.html')
        
        
        
       
