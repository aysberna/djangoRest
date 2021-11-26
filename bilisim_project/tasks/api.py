from tasks.models import Task
from rest_framework import serializers, viewsets, permissions
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer