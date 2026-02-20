from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from checkin.models import MoodEntry
from .ollama_client import get_ollama_response


def build_prompt(conversation, today_status):
    prompt = (
        "You are MindMate, a gentle mental wellness assistant. "
        "Provide calm, supportive responses. "
        "Do not give medical advice.\n\n"
    )

    if today_status:
        prompt += (
            f"User mental status today: "
            f"Mood={today_status.mood}, "
            f"Stress={today_status.stress_level}/5, "
            f"Energy={today_status.energy_level}, "
            f"Sleep={today_status.sleep_quality}.\n\n"
        )

    prompt += "Conversation so far:\n"

    for msg in conversation:
        prompt += f"{msg['role']}: {msg['content']}\n"

    prompt += "MindMate, respond kindly and briefly.\n"

    return prompt


@login_required
def chatbot_view(request):
    today = date.today()
    today_status = MoodEntry.objects.filter(
        user=request.user,
        date=today
    ).first()

    # Initialize conversation in session
    if 'conversation' not in request.session:
        request.session['conversation'] = []

    conversation = request.session['conversation']

    if request.method == 'POST':
        user_message = request.POST.get('message')

        # Add user message
        conversation.append({
            "role": "User",
            "content": user_message
        })

        prompt = build_prompt(conversation, today_status)
        bot_reply = get_ollama_response(prompt)

        # Add bot response
        conversation.append({
            "role": "MindMate",
            "content": bot_reply
        })

        request.session['conversation'] = conversation

    return render(request, 'chatbot.html', {
        'conversation': conversation
    })
