from django.contrib import admin
from django.urls import path
from .views import Lista
urlpatterns = [
    path('Productos/', Lista.as_view()),


]
