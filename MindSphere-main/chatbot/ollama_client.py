import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"   # faster model


def get_ollama_response(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 120   # limit response length
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=180  # ⬅️ increased timeout (3 minutes)
        )
        response.raise_for_status()

        data = response.json()
        return data.get("response", "I'm here with you.")

    except requests.exceptions.Timeout:
        return "I’m still thinking… please try again in a moment 🌱"

    except Exception as e:
        print("Ollama error:", e)
        return "I’m here, but something went wrong. Please try again."
