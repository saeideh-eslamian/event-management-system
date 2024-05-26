from django.contrib import admin
from django import forms
from events.models import Event
from django.contrib.auth.models import User


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'capacity']
    search_fields = ['title', 'location']
    exclude = ('attendees',)


admin.site.register(Event, EventAdmin)
