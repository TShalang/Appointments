from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.appointment_form),
    path('list/',views.appointment_list),
]