from app1.models import Person,Task
from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    contact = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=30)
    image = serializers.CharField(max_length=100)


    def create(self,validated_data):
        return Person.objects.create(**validated_data)

class TaskSerializer(serializers.ModelSerializer):
    class Meta():
        model = Task
        fields = '__all__'
