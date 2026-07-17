from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrManagerReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    # Apply our new custom RBAC rule
    permission_classes = [IsAuthenticated, IsOwnerOrManagerReadOnly] 

    def get_queryset(self):
        """
        Manager vs Employee Routing:
        Managers see the whole database. Employees only see their own rows.
        """
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)