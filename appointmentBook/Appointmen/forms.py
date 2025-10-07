from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['patient_name','doctor','age','date','time','symptoms']
        widgets={'date':forms.DateInput(attrs={"type":'date'}),
                 'time':forms.TimeInput(attrs={'type':'time'}),}


class SignUpForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

