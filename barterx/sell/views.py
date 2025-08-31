
from django.shortcuts import render, redirect
from .forms import ProductForm

def sell_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "sell.html", {"form": ProductForm(), "success": True})
    else:
        form = ProductForm()
    return render(request, "sell.html", {"form": form})


