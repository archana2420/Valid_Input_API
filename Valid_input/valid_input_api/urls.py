from django.contrib import admin
from django.urls import path,include
from .views import Valid_Input_APIView
urlpatterns = [
    path('',Valid_Input_APIView.as_view()),
]
