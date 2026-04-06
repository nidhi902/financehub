from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile

class SignupSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    access_code = serializers.CharField(required=False, allow_blank=True)  
      
    def create(self, validated_data):
        access_code=validated_data.pop('access_code', None)
        
        admin_code="ADMIN123"
        analyst_code="ANALYST123"
        role='user'
        if access_code and access_code not in [admin_code, analyst_code]:
            raise serializers.ValidationError("invalid access code")
        
        if access_code == admin_code:
            role='admin'
        elif access_code == analyst_code:
            role='analyst'
        
          
          
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, role=role)
        return user


class Loginserializer(serializers.Serializer):
    username = serializers.CharField()     
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError("Invalid username or password")

            if not user.is_active:
                raise serializers.ValidationError("User is inactive")

        else:
            raise serializers.ValidationError("Both username and password are required")
        
        return {"user": user}