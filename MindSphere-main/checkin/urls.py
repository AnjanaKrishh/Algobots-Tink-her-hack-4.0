from django.urls import path
from .views import mood_checkin, history

urlpatterns = [
    path('checkin/', mood_checkin, name='checkin'),
    path('history/', history, name='history'),
]
