from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
# Create your models here.
class User(AbstractUser):
    is_patient= models.BooleanField(default = False)
    is_doctor=models.BooleanField(default = False)
    
    def __str__(self):
        return self.username 
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def creat_auth_token(sender,instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance )
class Medicine(models.Model):
    price= models.IntegerField(default = 0)
    symptoms = models.CharField(max_length=200)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
class Patient(models.Model):
    medicine= models.ForeignKey(Medicine,on_delete = models.CASCADE)
    password2 = models.CharField(max_length=128,blank=True,null=True)
    blood=models.CharField(max_length=10,blank=True,null=True)
    case = models.CharField(max_length=20,blank=True,null=True)
    user = models.OneToOneField(User,related_name="patient",on_delete = models.CASCADE)
    name = models.CharField(max_length=40,blank=True)
    phone = models.CharField(max_length=12,default="",unique=True,blank=True,null=True)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=50,unique=True,blank=True)
    age = models.IntegerField(default= 0,blank=True,null=True )
    gender = models.CharField(max_length=30,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.user.username 
   	
class Docter(models.Model):
    name = models.CharField(max_length=40,blank=True,null=True)
    password = models.CharField(max_length=128,blank=True,null=True)
    password2 = models.CharField(max_length=128,blank=True,null=True)
    phone = models.CharField(max_length=12,default="",unique=True,blank=True,null=True)
    email = models.CharField(max_length=50,unique=True,blank=True,null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    age = models.IntegerField(default= 0,blank=True,null=True)
    blood = models.CharField(max_length=10,blank=True,null=True)
    user = models.OneToOneField(User,related_name="doctor",on_delete = models.CASCADE)
    status = models.BooleanField(default = 0,blank=True,null=True)
    department = models.CharField(max_length=30 , default = "",blank=True,null=True)
    attendance = models.IntegerField(default = 0,blank=True,null=True)
    salary = models.IntegerField(default = 10000,blank=True,null=True)
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE,unique = False)