from django.contrib.auth import authenticate, login, logout
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
    return render(request, 'document_page.html', {'students': students, 'username': auth.get_user(request).username})
    def example():
        personNames = ["Aliya", "Samal", "Safia", "Kamshat"]

        for pItr, p in enumerate(personNames):
            doc = DocxTemplate("inviteTmpl.docx")

            context = {
                "todayStr": "03.03.2023",
                "recipientName": p,
                "evntDtStr": "08.03.2023",
                "venueStr": "the beach",
                "bannerImg": ""
            }

            doc.render(context)

            doc.save("aaaa_{0}.docx".format(p))

def documents_second(request):
    students = Students.objects.all()
    return render(request, 'document_page_second.html', {'students': students, 'username': auth.get_user(request).username})

def documents_third(request):
    students = Students.objects.all()
    return render(request, 'document_page_third.html', {'students': students, 'username': auth.get_user(request).username})

def students(request):
    stud = Students.objects.all()
    return render(request, 'students.html', {'stud': stud, 'username': auth.get_user(request).username})

def commissions(request):
    return render(request, 'commissions.html', {'username': auth.get_user(request).username})
