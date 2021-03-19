from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'created', 'due_on', 'owner', 'mark')

class ShowTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
