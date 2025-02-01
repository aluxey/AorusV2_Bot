import os
import requests
from dotenv import load_dotenv

load_dotenv()

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
TWITCH_USER_ID = os.getenv("TWITCH_USER_ID")
TWITCH_OAUTH_TOKEN = os.getenv("TWITCH_ACCES_TOKEN")

def get_followed_streamers():
    """Fetch the list of streamers the user follows."""
    url = f"https://api.twitch.tv/helix/channels/followed?user_id={TWITCH_USER_ID}&first=100"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_OAUTH_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    print(f"🔍 DEBUG: Twitch API Response -> {response.json()}")  

    if response.status_code == 401:
        return "⚠️ Invalid OAuth token. Please refresh it."
    if response.status_code != 200:
        return f"Error: {response.json().get('message', 'Unknown error')}"

    follows = response.json().get("data", [])
    
    if not follows:
        return "You are not following any streamers."

    return [f"{follow['broadcaster_name']} (Twitch: {follow['broadcaster_login']})" for follow in follows]