
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from utils.config import GOOGLE_API_JSON

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(GOOGLE_API_JSON, scopes=SCOPES)
sheet_service = build('sheets', 'v4', credentials=creds)
SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"

def save_to_sheet(data: dict):
    try:
        sheet_service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body={"values": [[data.get("customer_name"), data.get("phone"),
                              data.get("car_issue"), data.get("preferred_time")]]}
        ).execute()
        return True
    except Exception as e:
        print(f"[SHEET ERROR] {e}")
        return False
