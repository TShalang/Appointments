# from appointments.forms import AppointmentForm
from django.shortcuts import render,redirect
from .forms import AppointmentForm
from .models import Appointment

# Create your views here.

def appointment_list(request):
    context = {'appointment_list':Appointment.objects.all()}
    return render(request,"appointments/appointment_list.html",context)

def appointment_form(request):
    if request.method == "GET":
        form = AppointmentForm()
        return render(request,"appointments/appointment_form.html",{'form':form})
    else: 
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/appointments/list')


