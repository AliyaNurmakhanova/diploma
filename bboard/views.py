from django.shortcuts import render
from django.http import HttpResponse

def login_page(request):
    return render(request, 'login_page.html')

def index(request):
    return render(request, 'index.html')

def basic(request):
    return render(request, 'basic.html')

def forgot_pw(request):
    return render(request, 'forgot_pw.html')