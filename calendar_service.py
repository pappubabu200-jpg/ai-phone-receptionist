
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from utils.config import GOOGLE_API_JSON

SCOPES = ["https://www.googleapis.com/auth/calendar"]
creds = Credentials.from_service_account_file(GOOGLE_API_JSON, scopes=SCOPES)
calendar_service = build('calendar', 'v3', credentials=creds)
CALENDAR_ID = "primary"

def create_calendar_event(data: dict):
    try:
        event = {
            'summary': f"Appointment: {data.get('customer_name')}",
            'description': f"Car issue: {data.get('car_issue')}",
            'start': {'dateTime': data.get('preferred_time'), 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': data.get('preferred_time'), 'timeZone': 'Asia/Kolkata'}
        }
        created_event = calendar_service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        return created_event
    except Exception as e:
        print(f"[CALENDAR ERROR] {e}")
        return None
