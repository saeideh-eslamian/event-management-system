from django.urls import path
from events import views

urlpatterns = [
    path('events/',views.EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
]
