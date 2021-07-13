from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePage(request):
    return render(request, "school/home.html")


def AboutPage(request):
    return render(request, "school/about.html")


def ContactUs(request):
    return render(request, "school/contact.html")


from .models import ExamScore


def ShowScore(request):
    score = ExamScore.objects.all()
    context = {"score": score}
    return render(request, "school/showscore.html", context)


from django.contrib.auth.models import User


def Register(request):
    if request.method == "POST":
        data = request.POST.copy()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
    return render(request, "school/register.html")
