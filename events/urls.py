from django.urls import path
from events import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('events/',views.EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
