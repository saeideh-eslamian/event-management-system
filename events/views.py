from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer
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
   