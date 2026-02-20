from django.db import models
from django.contrib.auth.models import User

class GameSession(models.Model):
    GAME_CHOICES = [
        ('memory', 'Memory Game'),
        ('reaction', 'Reaction Time'),
        ('focus', 'Focus Dot'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_type = models.CharField(max_length=20, choices=GAME_CHOICES)
    score = models.IntegerField(null=True, blank=True)
    time_taken = models.IntegerField(null=True, blank=True)  # seconds or ms
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game_type} - {self.created_at}"
