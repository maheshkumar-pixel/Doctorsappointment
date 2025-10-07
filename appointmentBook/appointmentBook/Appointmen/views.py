from .models import Appointment
from .forms import AppointmentForm
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('confirmation', appointment_id=appointment.id)  # ✅ Correct redirect
    else:
        form = AppointmentForm()
    return render(request, 'Appointmen/home.html', {'form': form})

def success(request):
    return render(request, 'Appointmen/success.html')

def confirmation(request, appointment_id):  # ✅ Add appointment_id to function parameters
    appointment = get_object_or_404(Appointment, pk=appointment_id)  # ✅ Use get_object_or_404 for safety
    return render(request, 'Appointmen/confirmation.html', {'appointment': appointment})  # ✅ Fix render line
