import logging
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from docxtpl import DocxTemplate
from django.contrib import auth

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden, HttpResponse

import io

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='secretary').exists():
                return redirect('bboard/index/')
            elif user.groups.filter(name='commission').exists():
                return redirect('bboard/commissions/')
            else:
                return redirect('/bboard')
        else:
            return render(request, 'login_page.html', {'error': 'Неправильное имя пользователя или пароль'})
    else:
        return render(request, 'login_page.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='secretary').exists())
def index(request):
    return render(request, 'index.html', {'username': auth.get_user(request).username})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='commission').exists())
def commissions(request):
    return render(request, 'commissions.html', {'username': auth.get_user(request).username})

def logout_page(request):
    logout(request)
    return redirect('login')

# def index(request):
#     return render(request, 'index.html', {'username': auth.get_user(request).username})

# def commissions(request):
#     return render(request, 'commissions.html', {'username': auth.get_user(request).username})

def student_page(request, id):
    student = get_object_or_404(Students, id=id)
    context = {
        'username': auth.get_user(request).username,
        'student': student
    }

    return render(request, 'student_page.html', context)

def download_document(request, stud_id):
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    student = get_object_or_404(Students, id=stud_id)
    context = {
        'student': student
    }
    name = student.name
    lastname = student.lastname
    middlename = student.middlename

    doc = DocxTemplate("bboard/static/protocol_2.docx")

    context = {
        "lastname": lastname,
        "name": name,
        "middlename": middlename,
        "speciality": "6B0602102 CS",
    }

    doc.render(context)

    doc.save("{0}_{1}_Протокол_2.docx".format(name, lastname))
    doc_name = f"{name}_{lastname}_Протокол_2.docx"
    logging.debug("Document name: {}".format(doc_name))
    print(doc_name)

    # Создать HTTP-ответ, который будет содержать созданный документ
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename={doc_name}'

    with io.open(doc_name, 'rb') as file:
        document_bytes = file.read()

    response['Content-Length'] = len(document_bytes)
    response.write(document_bytes)
    return response

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

    return render(request, 'document_page.html', {'students': students})


def documents_second(request):
    students = Students.objects.all()
    return render(request, 'document_page_second.html', {'students': students, 'username': auth.get_user(request).username})

def documents_third(request):
    students = Students.objects.all()
    return render(request, 'document_page_third.html', {'students': students, 'username': auth.get_user(request).username})

def students(request):
    students = Students.objects.all()
    context = {
        'username': auth.get_user(request).username,
        'students': students
    }
    return render(request, 'students.html', context)

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


# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.is_secretary:
#                 user.groups.add(Group.objects.get(name='secretaries'))
#                 login(request, user)
#                 return redirect('index.html')
#             elif user.is_commission:
#                 user.groups.add(Group.objects.get(name='commission'))
#             login(request, user)
#             return redirect('commissions.html')
#         else:
#             return render(request, 'login_page.html', {'error': 'Неправильное имя пользователя или пароль'})
#     else:
#         return render(request, 'login_page.html')

# @login_required(login_url='/login/')
# def index(request):
#     if request.user.is_secretary:
#         return render(request, 'index.html', {'username': auth.get_user(request).username})
#     else:
#         return redirect('login_page.html')
#
# @login_required(login_url='/login/')
# def commissions(request):
#     if request.user.is_commission:
#         return render(request, 'commissions.html', {'username': auth.get_user(request).username})
#     else:
#         return redirect('login_page.html')

# def is_secretary(user):
#     return user.groups.filter(name='secretaries').exists()
#
# @user_passes_test(is_secretary)
# @login_required
# def index(request):
#     return render(request, 'index.html', {'username': auth.get_user(request).username})
#
# def is_commission(user):
#     return user.groups.filter(name='commission').exists()
#
# @user_passes_test(is_commission)
# @login_required
# def commissions(request):
#     return render(request, 'commissions.html', {'username': auth.get_user(request).username})