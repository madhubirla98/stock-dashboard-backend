import requests
import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

def get_firebase_token(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("✅ ID Token:")
        print(data["idToken"])
        return data["idToken"]
    else:
        print("❌ Error logging in:", response.json())
        return None

# 🔧 Replace with your test user credentials
email = "madhubala.mnnit.2020@gmail.com"
password = "Madbir@98"

get_firebase_token(email, password)
