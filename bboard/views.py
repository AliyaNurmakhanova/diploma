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

def documents(request):
    students = Students.objects.all()
    return render(request, 'document_page.html', {'students': students})
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
    return render(request, 'document_page_second.html', {'students': students})

def documents_third(request):
    students = Students.objects.all()
    return render(request, 'document_page_third.html', {'students': students})

def students(request):
    stud = Students.objects.all()
    return render(request, 'students.html', {'stud': stud})

def commissions(request):
    return render(request, 'commissions.html')