from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    capacity = models.IntegerField()
    attendees = models.ManyToManyField(User, related_name='events')

    def __str__(self):
        return f"{self.title} date of event: {self.date}"
