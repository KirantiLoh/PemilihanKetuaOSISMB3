from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("Home")
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect("admin:index")
                else:
                    try:
                        student = Student.objects.get(user = user)
                        if student.voted == False:
                            login(request, user)
                            return redirect('Vote')
                    except ObjectDoesNotExist:
                        try:
                            teacher = Teacher.objects.get(user = user)
                            if teacher.voted == False:
                                login(request, user)
                                return redirect("Vote")
                            return redirect("Error", id = 2)
                        except ObjectDoesNotExist:
                            return redirect("Error", id = 3)
    return render(request, "login.html", {'form':form})

@login_required(login_url='Login')
def logout_view(request):
    try:
        student = Student.objects.get(user=request.user)
        if student.voted:
            logout(request)
            return redirect("Success")
        else:
            return redirect("Error",id=1)
    except ObjectDoesNotExist:
        teacher = Teacher.objects.get(user=request.user)
        if teacher.voted:
            logout(request)
            return redirect('Success')
        else:
            return redirect("Error", id=1)

@login_required(login_url='Login')
def set_voted_to_false(request):
    if request.user.is_superuser:
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        for student in students:
            student.voted = False
            student.save()
        for teacher in teachers:
            teacher.voted = False
            teacher.save()
        return redirect('admin:index')
    return redirect("Error", id = 5)

@login_required(login_url='Login')
def set_student_voted_to_true(request):
    if request.user.is_superuser:
        students = Student.objects.all()
        for student in students:
            student.voted = True
            student.save()
        return redirect('admin:index')
    return redirect("Error", id = 5)

@login_required(login_url='Login')
def set_teacher_voted_to_true(request):
    if request.user.is_superuser:
        teachers = Teacher.objects.all()
        for teacher in teachers:
            teacher.voted = False
            teacher.save()
        return redirect('admin:index')
    return redirect("Error", id = 5)