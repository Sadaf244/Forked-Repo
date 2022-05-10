from rest_framework.permissions import BasePermission
from .models import *
class IsDoctorUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_doctor)

class IsPatientUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_patient)