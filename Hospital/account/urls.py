from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('signup/doctor/',DoctorSignupView.as_view()),
    path('signup/patient/',PatientSignupView.as_view())
]
