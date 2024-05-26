from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from events.models import Event
from events.serializers import EventSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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


class JoinEventView(generics.GenericAPIView):
    """user can join to events if user is sign in"""
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if request.user in event.attendees.all():
            return Response(
                {'detail': 'You have already joined this event.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        event.attendees.add(request.user)
        event.save()
        return Response(
            {'detail': 'You have joined the event.'}, status=status.HTTP_200_OK
        )
    
class LeaveEventView(generics.GenericAPIView):
    """user can leave events if user is sign in"""
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk) 
        if request.user not in event.attendees.all():
            return Response(
                {'detail': 'You are not a member of this event.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        event.attendees.remove(request.user)
        event.save()
        return Response(
            {'detail': 'You have left the event.'}, status=status.HTTP_200_OK
            ) 

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
