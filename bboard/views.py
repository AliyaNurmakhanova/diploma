from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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

def student_page(request, id):
    student = get_object_or_404(Students, id=id)
    context = {
        'username': auth.get_user(request).username,
        'student': student
    }
    return render(request, 'student_page.html', context)

def edit_stud_page(request):
    return render(request, 'edit_stud_page.html', {'username': auth.get_user(request).username})

def forgot_pw(request):
    return render(request, 'forgot_pw.html')

def documents(request):
    students = Students.objects.all()
    return render(request, 'document_page.html', {'students': students})

def documents_second(request):
    students = Students.objects.all()
    return render(request, 'document_page_second.html', {'students': students})

def documents_third(request):
    students = Students.objects.all()
    return render(request, 'document_page_third.html', {'students': students})

# def students(request):
#     return render(request, 'students.html')

# def commissions(request):
#     return render(request, 'commissions.html')

# def documents(request):
#     return render(request, 'documents.html')

def students(request):
    students = Students.objects.all()
    return render(request, 'students.html', {'students': students})

def commissions(request):
    return render(request, 'commissions.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        middlename = request.POST.get('middlename')
        birthday = request.POST.get('birthday')
        diploma_title = request.POST.get('diploma_title')

        stud = Students(
            name = name,
            lastname = lastname,
            middlename = middlename,
            birthday = birthday,
            diploma_title = diploma_title
        )
        stud.save()
        return redirect('students_list')
    return render(request, 'students.html')