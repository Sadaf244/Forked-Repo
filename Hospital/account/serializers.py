# from django.contrib.auth import authenticate, get_user_model
# from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import *
# from django.contrib.auth import authenticate

# User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['user','email','is_doctor']
class PatientSignupSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={"input_type":"password"},write_only=True)
   
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write_only'}}
    def save(self,**kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        # password2=self.validated_data['password2']
        
        user.set_password(password)
        user.is_patient=True
        user.save()
        Patient.objects.create(user=user)
        return user
class DoctorSignupSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={"input_type":"password"},write_only=True,)
   
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write_only'}}
    def save(self,**kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        # password2=self.validated_data['password2']
        # if password!=password2:
        #     raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_doctor=True
        user.save()
        Docter.objects.create(user=user)
        return user

# class PatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Patient
#         fields="__all__"


    

