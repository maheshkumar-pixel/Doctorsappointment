from django.contrib import admin
from .models import Appointment,Doctor_Info

admin.site.register(Doctor_Info)
admin.site.register(Appointment)