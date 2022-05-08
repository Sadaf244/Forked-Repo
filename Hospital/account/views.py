from . serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

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
# class LoginAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = DocterSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"status": status.HTTP_200_OK, "Token": token.key})
# # def register(request) :
# # 	if request.method == 'POST':
# # 		print(request.POST['name'])
# # 		print(request.POST['post'])
# # 		try:
# # 			user = User.objects.get(username=request.POST['username'])
# # 			print(user)
# # 			return render(request,'register.html')
# # 		except User.DoesNotExist:
# # 			user = User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'])
# # 			if request.POST['post'] == 'Patient':
# # 				new = Patient(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user)	
# # 				new.save()	
# # 			else:
# # 				new = Docter(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user)	
# # 				new.save()	
				
	
# # 			print('Registered Successfully')
			
# # 	else:
# # 		return render(request , 'register.html')


# # # Login
# # def login(request):
# # 	if request.method == 'POST':
# # 		try:
# #  			# Check User in DB
# # 	 		uname = request.POST['username']
# # 	 		pwd = request.POST['pass1']
# # 	 		user_authenticate = auth.authenticate(username=uname,password=pwd)
# # 	 		if user_authenticate != None:
# # 	 			user = User.objects.get(username=uname)
# # 	 			try:
# # 	 				data = Patient.objects.get(username = user)
# # 	 				print(data)
# # 	 				print('Patient has been Logged')
# # 	 				auth.login(request,user_authenticate)				
# # 	 				return redirect('dashboard',user= "P")
# # 	 			except:
# # 	 				try:
# # 	 					data = Docter.objects.get(username = user )
# # 	 					auth.login(request,user_authenticate)				
# # 	 					print('Docter has been Logged')
# # 	 					return redirect('dashboard',user = "D")	 					
# # 	 				except:
# # 	 					try:
# # 		 					data = Receptionist.objects.get(username = user )
# # 		 					auth.login(request,user_authenticate)				
# # 		 					print('Receptionist has been Logged')
# # 		 					return redirect('receptionist_dashboard',user = "R")
# # 		 				except:
# # 		 					try:
# # 		 						data = HR.objects.get(username = user )
# # 		 						auth.login(request,user_authenticate)				
# # 		 						print('HR has been Logged')
# # 		 						return redirect('dashboard',user = "H")
# # 		 					except:
# # 		 						return redirect('/')

		 					
	 					
# # 	 		else:
# # 	 			print('Login Failed')
# # 	 			return render(request,'login.html')
# # 		except:
# # 	 		return render(request,'login.html')
# # 	return render(request , 'login.html')

# # # Logout
# # def logout(request):
# # 	auth.logout(request)
# # 	print('Logout')
# # 	return redirect('/login')
