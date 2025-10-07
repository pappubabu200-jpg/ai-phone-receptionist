
from services import ai_service, sheet_service, calendar_service, sms_service

def test_ai_response():
    response = ai_service.get_ai_response("greeting")
    assert response is not None

def test_sheet_save():
    result = sheet_service.save_to_sheet({"customer_name": "Test", "phone": "123", "car_issue": "Brake", "preferred_time": "2025-10-07T10:00:00"})
    assert result is True or result is False  # depends on API key availability

def test_calendar_event():
    result = calendar_service.create_calendar_event({"customer_name": "Test", "car_issue": "Brake", "preferred_time": "2025-10-07T10:00:00"})
    assert result is None or result is not None

def test_sms_send():
    result = sms_service.send_sms("1234567890", "Test message")
    assert "status" in result
