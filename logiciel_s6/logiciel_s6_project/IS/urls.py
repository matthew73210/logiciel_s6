from django.urls import path, include
from rest_framework import routers

#from . import api
from . import views


urlpatterns = [
    
    path('', views.index, name="IS")
    
]
