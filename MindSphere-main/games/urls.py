from django.urls import path
from .views import (
    games_home,
    breathing_game,
    thought_clear_game,
    memory_game,
    reaction_game,
    focus_dot_game
)

urlpatterns = [
    path('', games_home, name='games_home'),
    path('breathing/', breathing_game, name='breathing_game'),
    path('thought-clear/', thought_clear_game, name='thought_clear_game'),
    path('memory/', memory_game, name='memory_game'),
    path('reaction/', reaction_game, name='reaction_game'),
    path('focus-dot/', focus_dot_game, name='focus_dot_game'),
]
