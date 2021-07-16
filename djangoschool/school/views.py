from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
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


from django.core.files.storage import FileSystemStorage
from .models import Profile


@login_required
def EditProfile(request):
    username = request.user.username
    current = User.objects.get(username=username)

    if request.method == "POST" and request.FILES["photoprofile"]:
        data = request.POST.copy()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        myprofile = User.objects.get(username=username)
        try:
            setprofile = Profile.objects.get(user=myprofile)
        except:
            setprofile = Profile()
            setprofile.user = myprofile

        file_image = request.FILES["photoprofile"]
        file_image_name = request.FILES["photoprofile"].name
        fs = FileSystemStorage()
        filename = fs.save(file_image_name, file_image)
        upload_file_url = fs.url(filename)
        setprofile.photoprofile = upload_file_url[6:]
        setprofile.save()

        myprofile = User.objects.get(username=username)
        myprofile.username = email
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.email = email
        myprofile.save()

        return redirect("edit-profile")
    context = {"data": current}
    return render(request, "school/editprofile.html", context)


def ShowDocument(request):
    document = DocumentUpload.objects.all()
    context = {"document": document}
    return render(request, "school/document.html", context)
