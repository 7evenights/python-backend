from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ExamScore, AllStudent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def HomePage(request):
    return render(request, "school/home.html")


def AboutPage(request):
    return render(request, "school/about.html")


def ContactUs(request):
    return render(request, "school/contact.html")


def ShowScore(request):
    score = ExamScore.objects.all()
    context = {"score": score}
    return render(request, "school/showscore.html", context)


def Register(request):
    if request.method == "POST":
        data = request.POST.copy()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.set_password(password)
        newuser.save()
        return redirect("home-page")

    return render(request, "school/register.html")


@login_required
def SearchStudent(request):
    # search = AllStdeunt.object.get(student_id='')
    if request.method == "POST":
        data = request.POST.copy()
        searchid = data.get("search")
        try:
            result = AllStudent.objects.get(student_id=searchid)
            context = {"result": result, "check": "found"}
        except:
            context = {"result": "ไม่มีข้อมูลในระบบ", "check": "notfound"}
        return render(request, "school/search.html", context)

    return render(request, "school/search.html")
