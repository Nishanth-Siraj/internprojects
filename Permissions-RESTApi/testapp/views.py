from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserTestSerializer
from .models import CustomUser
from .permissions import islevel1

class BaseSettings(APIView):
    permission_classes = [IsAuthenticated, islevel1]

class ListCreateUsers(BaseSettings, ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserTestSerializer