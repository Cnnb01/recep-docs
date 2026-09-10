from django.urls import path, include
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
]
