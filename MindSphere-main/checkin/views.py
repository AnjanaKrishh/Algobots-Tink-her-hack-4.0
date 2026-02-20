from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodForm
from .models import MoodEntry
from games.models import GameSession
from datetime import date


@login_required
def mood_checkin(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = MoodForm()

    return render(request, 'checkin.html', {'form': form})


@login_required
def history(request):
    mood_entries = MoodEntry.objects.filter(
        user=request.user
    ).order_by('-date')

    history_data = []

    total_stress = 0

    for mood in mood_entries:
        # Games played on the same date
        games = GameSession.objects.filter(
            user=request.user,
            created_at=mood.date
        )

        total_stress += mood.stress_level

        history_data.append({
            'date': mood.date,
            'mood': mood.mood,
            'stress': mood.stress_level,
            'energy': mood.energy_level,
            'sleep': mood.sleep_quality,
            'games': games
        })

    # Average stress calculation (overall)
    avg_stress = None
    status = "No Data"
    color = "gray"

    if mood_entries.exists():
        avg_stress = round(total_stress / mood_entries.count(), 2)

        if avg_stress >= 4:
            status = "High Stress"
            color = "red"
        elif avg_stress >= 2.5:
            status = "Moderate Stress"
            color = "orange"
        else:
            status = "Low Stress"
            color = "green"

    return render(request, 'history.html', {
        'history': history_data,
        'avg_stress': avg_stress,
        'status': status,
        'color': color
    })
