from rest_framework import serializers

from task_tracker.models import Task


class Task(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
