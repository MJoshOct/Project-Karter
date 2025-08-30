from django.shortcuts import render,get_object_or_404,redirect
from .models import Question
from .forms import QuestionForm,AnswerForm

# Create your views here.

def question_list(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "forum/question_list.html", {"questions": questions})

def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)

    # Handle posting an answer
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            if request.user.is_authenticated:
                answer.author = request.user
            else:
                answer.author = None
            answer.question = question
            answer.save()
            return redirect("question_detail", slug=question.slug)
    else:
        answer_form = AnswerForm()

    return render(
        request,
        "forum/question_detail.html",
        {"question": question, "answer_form": answer_form},
    )

def ask_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
           # question.author = request.user  # attach the logged-in user
            # only set author if logged in
            if request.user.is_authenticated:
                question.author = request.user
            question.save()
            form.save_m2m()  # for tags
            return redirect("question_detail", slug=question.slug)
    else:
        form = QuestionForm()
    return render(request, "forum/ask_question.html", {"form": form})
