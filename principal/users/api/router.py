from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import userApiViewset

routers_users=DefaultRouter() 
routers_users.register(prefix ='users',
                       viewset=userApiViewset, basename='users')