from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials

load_dotenv()

cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not cred_path or not os.path.exists(cred_path):
    raise RuntimeError("Invalid or missing GOOGLE_APPLICATION_CREDENTIALS")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
