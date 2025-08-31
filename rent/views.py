from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product, RentRequest

# Rent/Request page
@login_required
def rent_request_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    suggestions = Product.objects.exclude(id=product.id)[:3]  # suggest other items

    if request.method == "POST":
        duration_value = int(request.POST.get("durationValue"))
        duration_unit = request.POST.get("unit")
        notes = request.POST.get("notes", "")

        # Rent rates mapping
        rent_rates = {
            "hour": 50,
            "day": 299,
            "week": 1500,
            "month": 5000,
        }
        rate = rent_rates.get(duration_unit, 299)
        total_cost = duration_value * rate

        # Save rent request (transaction record)
        RentRequest.objects.create(
            user=request.user,
            product=product,
            duration_value=duration_value,
            duration_unit=duration_unit,
            notes=notes,
            total_cost=total_cost,
            date_requested=timezone.now(),
        )

        return render(request, "requestRent.html", {
            "product": product,
            "suggestions": suggestions,
            "confirmation": f"Request submitted for {duration_value} {duration_unit}(s). Total Rent: ₹{total_cost}. Notes: {notes}",
        })

    return render(request, "requestRent.html", {
        "product": product,
        "suggestions": suggestions,
    })
