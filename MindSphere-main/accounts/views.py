from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from checkin.models import MoodEntry
from datetime import date

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    today_status = MoodEntry.objects.filter(
        user=request.user,
        date=date.today()
    ).first()

    return render(request, 'dashboard.html', {
        'today_status': today_status
    })
