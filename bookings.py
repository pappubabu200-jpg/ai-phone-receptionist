
from fastapi import APIRouter
from services import sheet_service, calendar_service, sms_service

router = APIRouter()

@router.post("/create")
def create_booking(data: dict):
    sheet_service.save_to_sheet(data)
    calendar_service.create_calendar_event(data)
    sms_service.send_sms("OWNER_PHONE_NUMBER", f"New booking: {data}")
    return {"status": "success", "data": data}
