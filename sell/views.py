from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
import random

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

def home(request):
    # Suggested items (randomized)
    all_items = list(Product.objects.all())
    suggested_items = random.sample(all_items, min(len(all_items), 10))

    # Handle search
    query = request.GET.get("q")
    results = []
    if query:
        results = Product.objects.filter(title__icontains=query)

    return render(request, "home/homepage.html", {
        "suggested_items": suggested_items,
        "results": results,
        "query": query,
    })
