from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # This ensures the user field is read-only so someone can't assign a task to another user via the API
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at']