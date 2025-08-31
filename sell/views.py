from django.shortcuts import render, redirect
from .forms import ProductForm

def sell(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("sell_success")
    else:
        form = ProductForm()
    
    return render(request, "sell/sell.html", {"form": form})

def sell_success(request):
    return render(request, "sell/sell_success.html")
