from .import views
from django.urls import path

urlpatterns=[
    path("home/",views.home,name='home'),
    path("sucess/",views.success,name='success'),
    path('confirmation/<int:appointment_id>/', views.confirmation, name='confirmation'),
    path('', views.signup_view, name='signup'),path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


]