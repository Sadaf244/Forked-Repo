from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('signup/doctor/',DoctorSignupView.as_view()),
    path('signup/patient/',PatientSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(),name="auth-token"),
    path('profileview/<int:pk>',DoctorProfileView.as_view(),name="profile"),
    path('patientprofileview/<int:pk>',PatientProfileView.as_view(),name="patientprofile"),
    path('medicine',MedicineView.as_view(),name="medicinelist"),
    path('patientview',DoctorPatientView.as_view(),name="patientlist"),
    path('logout/',LogoutView.as_view(),name="logout")
]

