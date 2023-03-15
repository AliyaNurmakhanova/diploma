from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Students
from docxtpl import DocxTemplate

def login_page(request):
    return render(request, 'login_page.html')

def index(request):
    return render(request, 'index.html')

def student_page(request):
    return render(request, 'student_page.html')

def edit_stud_page(request):
    return render(request, 'edit_stud_page.html')

def forgot_pw(request):
    return render(request, 'forgot_pw.html')

<<<<<<< HEAD
def documents(request):
    students = Students.objects.all()
    return render(request, 'document_page.html', {'students': students})

=======
def students(request):
    return render(request, 'students.html')

def commissions(request):
    return render(request, 'commissions.html')

def documents(request):
    return render(request, 'documents.html')
>>>>>>> 2944f1b15c565ef153aaa3a248579e136977aa67
