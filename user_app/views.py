from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import Loginserializer, SignupSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import Loginserializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Profile

# def home(request):
#     return HttpResponse("User OK ✅")
# views.py


def home(request):
    return HttpResponse("Welcome to StudyHub! Please signup to continue.")
class Signupview(APIView):
    def post(Self, request):
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message: user created succesfully"})
        return Response(serializer.errors, status=400)
    
    # def get(self, request):
    #     userr=User.objects.all()
    #     serializer=SignupSerializer(userr, many=True)
    #     return Response(serializer.data, status=200)
        
class loginview(APIView):
    def post(self, request):
        serializer=Loginserializer(data=request.data) 
        if serializer.is_valid():
            user=serializer.validated_data['user']       
            
            token, created = Token.objects.get_or_create(user=user)

            # Step 5: response dena
            return Response({
                "token": token.key,
                "username": user.username,
                "role": user.profile.role   # ya is_staff agar default user model hai
            })

        # invalid case
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)