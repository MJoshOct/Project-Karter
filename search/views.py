# search/views.py
from django.db.models import Q
from django.shortcuts import render
# from sell.models import Item    
from forum.models import Question
   

def search(request):
    
    query = request.GET.get("q", "").strip()
    results = []
    search_type = request.GET.get("type", "forum") 
    

    if query:
        if search_type == "forum":
            results = Question.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
            context_type = "forum"


    return render(request, "search/results.html", {
        "query": query,
        "results": results,
        "search_type": search_type,
    })
