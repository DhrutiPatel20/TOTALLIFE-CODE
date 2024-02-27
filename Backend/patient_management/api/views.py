from django.shortcuts import render

# Create your views here.
from rest_framework import generics, serializers
from .models import Clinician, Patient, Appointment
from .serializers import ClinicianSerializer, PatientSerializer, AppointmentSerializer

class ClinicianListCreateView(generics.ListCreateAPIView):
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

class ClinicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer