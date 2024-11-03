from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router = DefaultRouter()
router.register('students', ListView, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'),

]
