from django.urls import path
from .views import ClinicianListCreateView, ClinicianDetailView, PatientListCreateView, PatientDetailView, AppointmentListCreateView, AppointmentDetailView

urlpatterns = [
    path('clinicians/', ClinicianListCreateView.as_view(), name='clinician-list-create'),
    path('clinicians/<int:pk>/', ClinicianDetailView.as_view(), name='clinician-detail'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),]
