
from twilio.rest import Client
from utils.config import TWILIO_SID, TWILIO_AUTH, TWILIO_NUMBER

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_sms(to: str, message: str):
    try:
        msg = client.messages.create(body=message, from_=TWILIO_NUMBER, to=to)
        return {"status": "sent", "sid": msg.sid}
    except Exception as e:
        print(f"[SMS ERROR] {e}")
        return {"status": "failed", "error": str(e)}
