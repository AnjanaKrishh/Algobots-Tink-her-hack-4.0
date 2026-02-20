from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GameSession
from datetime import date


@login_required
def games_home(request):
    return render(request, 'games/home.html')

@login_required
def breathing_game(request):
    return render(request, 'games/breathing.html')

@login_required
def thought_clear_game(request):
    return render(request, 'games/thought_clear.html')

@login_required
def memory_game(request):
    return render(request, 'games/memory.html')

@login_required
def reaction_game(request):
    if request.method == 'POST':
        score = int(request.POST.get('reaction_time'))
        GameSession.objects.create(
            user=request.user,
            game_type='reaction',
            score=score
        )
    return render(request, 'games/reaction.html')

@login_required
def focus_dot_game(request):
    return render(request, 'games/focus_dot.html')

