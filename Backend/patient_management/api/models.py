from django.db import models

# Create your models here.
from django.db import models
import requests
class Clinician(models.Model):
    npi_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    state = models.CharField(max_length=2, blank=True, null=True)
    # Add other relevant fields



class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

class Appointment(models.Model):
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
