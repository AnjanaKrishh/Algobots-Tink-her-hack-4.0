from django import forms
from .models import MoodEntry

class MoodForm(forms.ModelForm):
    stress_level = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Stress Level (1 = Low, 5 = High)"
    )

    class Meta:
        model = MoodEntry
        fields = [
            'mood',
            'stress_level',
            'energy_level',
            'sleep_quality',
            'note'
        ]
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3}),
        }
