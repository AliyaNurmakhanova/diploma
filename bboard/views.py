from django.shortcuts import render, redirect
from django.http import HttpResponse

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
