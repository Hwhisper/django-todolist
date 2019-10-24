
from rest_framework import serializers
from .models import Todo

# modal change JSON
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
