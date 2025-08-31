from django.shortcuts import render,get_object_or_404
from sell.models import Product  
from django.db.models import QuerySet

def homepage(request):
    # --- Search (title only) ---
    query = (request.GET.get("q") or "").strip()
    results: QuerySet[Product] = Product.objects.none()
    suggestions_qs: QuerySet[Product] = Product.objects.all()

    if query:
        results = Product.objects.filter(title__icontains=query)
        
        suggestions_qs = suggestions_qs.exclude(id__in=results.values_list("id", flat=True))

    
    suggested_items = list(suggestions_qs.order_by("?")[:20])

    return render(
        request,
        "home/homepage.html",
        {
            "query": query,
            "results": results,
            "suggested_items": suggested_items,
        },
    )
