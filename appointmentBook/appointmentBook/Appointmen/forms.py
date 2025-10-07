from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['patient_name','doctor','age','date','time','symptoms']
        widgets={'date':forms.DateInput(attrs={"type":'date'}),
                 'time':forms.TimeInput(attrs={'type':'time'}),}
