from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from.models import Student,Course
from.forms import StudentForm, RegisterForm, CourseForm

# Create your views here.
# def home(request):
#     return HttpResponse("welcome to the home page")
# def about(request):
#     return HttpResponse("this is the about page for students")
# def contact(request):
#     return HttpResponse("<h1>contact page</h1><p>phone:123-456-789") 
# def greet(request):
#     return HttpResponse("hello everyone!...")

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def profile(request):
    context={
        "title":"welcome san!",
        "msg":"this is dynamic content from django."
    }
    return render(request,"profile.html",context)
def feedback(request):
    return render(request,"feedback.html")
def gallery(request):
    return render(request,"gallery.html")

def list_students(request):
    data = Student.objects.all()
    return render(request,"list_students.html",{"students":data})

def students_list(request):
    data = Student.objects.all()
    return render(request,"students_list.html",{"students":data})

def add_students(request):
    if request.method == "POST":
        form = StudentForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form =StudentForm()
    return render(request,"add_students.html",{"form":form}) 

def edit_students(request,id):
    students =get_object_or_404(Student,id=id)
    if request.method =="POST":
        form = StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form =StudentForm(instance=students)  
    return render(request,"edit_students.html",{"form":form}) 

def delete_students(request,id):
    students=get_object_or_404(Student,id=id)
    students.delete()
    return redirect('/students/')

def course_list(request):
    data=Course.objects.all()
    return render(request,"course_list.html",{"course":data})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "add_course.html", {"form": form})


def edit_course(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(instance=course)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")

    return render(request, "edit_course.html", {"form": form})


def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect("course_list")


def active_course(request):
    course = Course.objects.filter(active=True)
    return render(request, "active_course.html", {"courses": course})

def register_User(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=RegisterForm()
        return render(request,"register.html",{"form":form})
    
def login_User(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            Username=form.cleaned_data.get("Username")
            Password=form.cleaned_data.get("Password")
            User=authenticate(Username=Username,Password=Password)
        if User:
            login(request,User)
            return redirect('/dashboard/')
    else:
        form=AuthenticationForm()
        return render(request,"login.html",{"form":form}) 
    
def logout_User(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url="/login/")
def dashboard(request):
    return render(request,"dashboard.html")