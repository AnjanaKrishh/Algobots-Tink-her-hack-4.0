from django.urls import path
from .views import dashboard


urlpatterns = [
    path('signup/', signup, name='signup'),
]
