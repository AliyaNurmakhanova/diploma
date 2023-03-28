from django.urls import path, re_path
from bboard import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page, name='login'),
    path('/logout/', views.logout_page, name='logout'),
    path('/index/', views.index, name='index'),
    path('/forgot/', views.forgot_pw, name='forgot'),
    path('/documents/', views.documents, name='documents'),
    path('student/<int:id>/', views.student_page, name='student_page'),
    path('/edit_stud/', views.edit_stud_page, name='edit_stud'),
    path('/students/', views.students, name='students_list'),
    path('/commissions/', views.commissions, name='commissions_list'),
    path('/documents/', views.documents, name='documents_list'),
    path('/documentssecond/', views.documents_second, name='documents_list_second'),
    path('/documentsthird/', views.documents_third, name='documents_list_third'),
    path('/add/', views.add_student, name='add_students'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)