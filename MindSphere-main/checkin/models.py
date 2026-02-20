from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):

    MOOD_CHOICES = [
        ('happy', 'Happy 😊'),
        ('neutral', 'Neutral 😐'),
        ('sad', 'Sad 😔'),
        ('stressed', 'Stressed 😫'),
    ]

    ENERGY_CHOICES = [
        ('high', 'High ⚡'),
        ('medium', 'Medium 🙂'),
        ('low', 'Low 😴'),
    ]

    SLEEP_CHOICES = [
        ('good', 'Good 😌'),
        ('average', 'Average 😐'),
        ('poor', 'Poor 😵'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    stress_level = models.IntegerField(help_text="1 (Low) to 5 (High)")
    energy_level = models.CharField(max_length=10, choices=ENERGY_CHOICES)
    sleep_quality = models.CharField(max_length=10, choices=SLEEP_CHOICES)

    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
