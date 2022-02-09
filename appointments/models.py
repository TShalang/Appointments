from django.db import models

# Create your models here.

class Appointment(models.Model):
    student_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50)
    app_date = models.DateField()
    app_desc = models.CharField(max_length=100)