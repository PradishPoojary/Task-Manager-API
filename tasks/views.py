from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Locks down the endpoint to JWT holders only

    def get_queryset(self):
        """
        Security Override: This ensures that when a user requests the list of tasks, 
        they ONLY get the tasks that belong to their specific user ID.
        """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Security Override: When a new task is created, automatically attach 
        the currently authenticated user to it.
        """
        serializer.save(user=self.request.user)