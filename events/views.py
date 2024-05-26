from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from events.models import Event
from events.serializers import EventSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EventListCreateView(generics.ListCreateAPIView):
    """show a list of all events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Used for read-write-delete endpoints to represent a single model instance."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
   

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        response.data['refresh'] = str(refresh)
        response.data['access'] = str(refresh.access_token)
        return response
