from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, choices=[
        ('general', 'General Practitioner'),
        ('cardiologist', 'Cardiologist'),
        ('dermatologist', 'Dermatologist'),
        ('dentist', 'Dentist'),
        ('pediatrician', 'Pediatrician'),
        ('psychiatrist', 'Psychiatrist'),
    ])
    clinic_name = models.CharField(max_length=100, choices=[
        ('city_clinic', 'City Clinic'),
        ('healthcare_center', 'Healthcare Center'),
        ('wellness_hub', 'Wellness Hub'),
        ('family_health', 'Family Health'),])
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Appointment for {self.patient} on {self.appointment_date}"
