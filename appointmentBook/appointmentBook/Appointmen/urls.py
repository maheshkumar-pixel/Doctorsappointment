from .import views
from django.urls import path

urlpatterns=[
    path("",views.home,name='home'),
    path("sucess/",views.success,name='success'),
    path('confirmation/<int:appointment_id>/', views.confirmation, name='confirmation'),

]