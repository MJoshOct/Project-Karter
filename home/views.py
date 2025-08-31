from django.shortcuts import render
from sell.models import Product  # ✅ import from the sell app
from django.db.models import QuerySet

def homepage(request):
    # --- Search (title only) ---
    query = (request.GET.get("q") or "").strip()
    results: QuerySet[Product] = Product.objects.none()
    suggestions_qs: QuerySet[Product] = Product.objects.all()

    if query:
        results = Product.objects.filter(title__icontains=query)
        # Exclude search results from suggestions
        suggestions_qs = suggestions_qs.exclude(id__in=results.values_list("id", flat=True))

    # --- Suggested (randomized, max 10) ---
    suggested_items = list(suggestions_qs.order_by("?")[:6])

    return render(
        request,
        "home/homepage.html",
        {
            "query": query,
            "results": results,
            "suggested_items": suggested_items,
        },
    )
