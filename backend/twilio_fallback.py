# backend/twilio_fallback.py
import os
from twilio.rest import Client 
from dotenv import load_dotenv

load_dotenv()

def send_fallback_sms(to, message):
    try:
        client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        from_number = os.getenv("TWILIO_PHONE")
        client.messages.create(to=to, from_=from_number, body=message)
        return True
    except Exception as e:
        print(f"Twilio Error: {e}")
        return False
