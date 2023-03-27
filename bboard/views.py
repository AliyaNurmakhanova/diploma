from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Students
from docxtpl import DocxTemplate
from django.contrib import auth

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login_page.html', {'error': 'Неправильное имя пользователя или пароль'})
    else:
        return render(request, 'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('/bboard')

def index(request):
    return render(request, 'index.html', {'username': auth.get_user(request).username})

def student_page(request):
    return render(request, 'student_page.html', {'username': auth.get_user(request).username})

def edit_stud_page(request):
    return render(request, 'edit_stud_page.html', {'username': auth.get_user(request).username})

def forgot_pw(request):
    return render(request, 'forgot_pw.html')

def documents(request):
    students = Students.objects.all()
    return render(request, 'document_page.html', {'students': students})

# def students(request):
#     return render(request, 'students.html')

# def commissions(request):
#     return render(request, 'commissions.html')

# def documents(request):
#     return render(request, 'documents.html')
