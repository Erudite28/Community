from django.shortcuts import render
from .models import User
from rest_framework import generics,status,permissions
from rest_framework_response import Response
from rest_framework_view import APIview
from rest_framework.simple_jwt.models import Token
from serializers import Userserializer,RegisterSerializer,LoginSerializer

class RegisterApi(generic.GenericAPIView):
    serializer_class=serializer