
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Transaction, Review
from django.utils import timezone

# Buy Page
def buy_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    suggestions = Product.objects.exclude(id=product.id)[:3]  # 3 suggested items

    if request.method == "POST" and "buy" in request.POST:
        qty = int(request.POST.get("quantity", 1))
        if qty <= product.stock:
            Transaction.objects.create(product=product, quantity=qty, date=timezone.now())
            product.stock -= qty
            product.save()
        return redirect("buy", product_id=product.id)

    if request.method == "POST" and "review" in request.POST:
        username = request.POST.get("username")
        message = request.POST.get("message")
        Review.objects.create(product=product, username=username, message=message)
        return redirect("buy", product_id=product.id)

    reviews = product.reviews.all().order_by("-date")
    return render(request, "buy.html", {"product": product, "reviews": reviews, "suggestions": suggestions})
