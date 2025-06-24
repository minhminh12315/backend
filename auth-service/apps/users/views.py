from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = request.data
            phone_number = data.get('phone_number')
            password = data.get('password')
            fullname = data.get('fullname')
            
            # Check if user exists
            if User.objects.filter(phone_number=phone_number).exists():
                return Response({
                    'error': 'User with this phone number already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Create user
            user = User.objects.create(
                phone_number=phone_number,
                fullname=fullname,
                password=make_password(password)
            )
            
            return Response({
                'message': 'User created successfully',
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'error': str(e)            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            phone_number = request.data.get('phone_number')
            password = request.data.get('password')

            if not phone_number or not password:
                return Response({
                    'error': 'Phone number and password are required.'
                }, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request, phone_number=phone_number, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'phone_number': user.phone_number
                })
            else:
                return Response({
                    'error': 'Invalid phone number or password.'
                }, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
