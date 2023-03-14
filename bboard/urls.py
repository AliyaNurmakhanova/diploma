from django.urls import path, re_path
from bboard import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('/index/', views.index, name='index'),
    path('/forgot/', views.forgot_pw, name='forgot'),
    path('/student/', views.student_page, name='student'),
    path('/edit_stud/', views.edit_stud_page, name='edit_stud'),
    path('/students/', views.students, name='students_list'),
    path('/commissions/', views.commissions, name='commissions_list'),
    path('/documents/', views.documents, name='documents_list'),
]
