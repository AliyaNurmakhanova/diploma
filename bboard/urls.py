from django.urls import path, re_path
from bboard import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('/index/', views.index, name='index'),
    path('/forgot/', views.forgot_pw, name='forgot'),
    path('/documents/', views.documents, name='documents'),
]
