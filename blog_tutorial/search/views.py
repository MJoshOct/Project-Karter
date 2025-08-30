from django.shortcuts import render
from blog.models import Post, Category   

def search(request):
    query = request.GET.get("q")
    results = []
    categories = Category.objects.all()   

    if query:
        results = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            body__icontains=query
        )

    return render(
        request,
        "search/results.html",
        {
            "results": results,
            "query": query,
            "categories": categories,
        },
    )
































