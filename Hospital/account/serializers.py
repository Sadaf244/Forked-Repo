from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import Medicine,Patient,Docter
from django.contrib.auth import authenticate

# User = get_user_model()

class DocterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Docter
        email = serializers.CharField(max_length=255)

        password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
        )
        def validate(self, data):
            username = data.get('email')
            password = data.get('password')
            
            if username and password:
                user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
                if not user:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg, code='authorization')
            
            else:
                msg = _('Must include "username" and "password".')
                raise serializers.ValidationError(msg, code='authorization')

            data['user'] = user
            return data
   
class MedicineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Medicine
        fields="__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"


    

