from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
#from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# Create your views here.
class ListView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]