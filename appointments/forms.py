from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {
            'student_number': 'Student Number',
            'student_name': 'Student Name',
            'app_date': 'Appointment Date',
            'app_desc': 'Appointment Description',

        }