from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

urlpatterns = [
    path('', include('tasks.urls')),
]
