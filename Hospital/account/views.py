from . serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.generic import CreateView, ListView, UpdateView

class DoctorSignupView(generics.GenericAPIView):
    serializer_class= DoctorSignupSerializer
    def post(self, request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created"
        })
class PatientSignupView(generics.GenericAPIView):
    serializer_class= PatientSignupSerializer
    def post(self, request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request,*args,**kwargs):
        serializer= self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response({
            "user_id":user.pk,
            "token":token.key,
            "is_doctor":user.is_doctor,
            "is_patient":user.is_patient
            
        })

    
    
