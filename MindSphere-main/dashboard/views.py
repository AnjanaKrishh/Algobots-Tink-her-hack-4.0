from django.contrib.auth.decorators import login_required
from checkin.models import MoodEntry
from datetime import date

@login_required
def dashboard(request):
    today = date.today()

    today_status = MoodEntry.objects.filter(
        user=request.user,
        date=today
    ).first()

    return render(request, 'dashboard.html', {
        'today_status': today_status
    })
