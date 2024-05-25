#Serializers are used to convert model instances to JSON and vice versa.

from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id','username','email']

class EventSerializer(serializers.ModelSerializer):
    attendees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'