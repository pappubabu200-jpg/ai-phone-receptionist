
from fastapi import APIRouter, Request
from services import ai_service
from twilio.twiml.voice_response import VoiceResponse

router = APIRouter()

@router.post("/incoming")
async def handle_call(request: Request):
    payload = await request.form()
    prompt = "greeting"
    response_text = ai_service.get_ai_response(prompt)
    twiml = VoiceResponse()
    twiml.say(response_text)
    return str(twiml)
