
from rest_framework import serializers

from .models import Clinician, Patient, Appointment

class ClinicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinician
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'