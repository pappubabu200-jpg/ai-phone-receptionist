
import os
from dotenv import load_dotenv
load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
OPENAI_KEY = os.getenv("OPENAI_KEY")
GOOGLE_API_JSON = os.getenv("GOOGLE_API_JSON")
