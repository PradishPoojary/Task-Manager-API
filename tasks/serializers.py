from rest_framework import serializers
from .models import Task, Tag

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # Accept a list of strings when creating/updating a task
    tag_inputs = serializers.ListField(
        child=serializers.CharField(max_length=50), write_only=True, required=False
    )
    # Output the linked tags as a clean list of strings when reading the data
    tags = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'status', 'tags', 'tag_inputs', 'created_at', 'updated_at']

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def create(self, validated_data):
        tags_data = validated_data.pop('tag_inputs', [])
        task = Task.objects.create(**validated_data)
        
        # Smart Tag Assignment: Get it if it exists in the DB, create it if it doesn't
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name.strip().upper())
            task.tags.add(tag)
            
        return task