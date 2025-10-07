from .models import Appointment
from .forms import AppointmentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'Appointmen/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Appointmen/login.html', {'error': "Invalid credentials"})
    return render(request, 'Appointmen/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



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
