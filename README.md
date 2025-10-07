# AI Phone Receptionist
Real API-ready project with OpenAI, Twilio, Google Sheets & Calendar.


## AI Phone Receptionist

Automated backend system for auto repair shops using AI and APIs.


---

Features

Handles incoming phone calls using Twilio.

AI-powered responses via OpenAI GPT-4.

Collects booking information: customer name, phone, car issue, preferred time.

Saves data to Google Sheets and Google Calendar.

Sends SMS notifications to shop owner via Twilio.

Mobile-friendly backend with FastAPI.

CI workflow for linting and testing included.



---

Tech Stack

FastAPI – Backend API framework

Python 3.11+

OpenAI GPT-4 – Natural language AI

Twilio API – Phone & SMS

Google Sheets & Calendar API – Booking management

GitHub Actions – CI workflow



---

Setup Instructions

1. Clone the repository:



git clone https://github.com/USERNAME/ai-phone-receptionist.git
cd ai-phone-receptionist

2. Install dependencies:



pip install -r backend/requirements.txt

3. Add environment variables in .env:



TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth
TWILIO_NUMBER=+123456789
OPENAI_KEY=your_openai_key
GOOGLE_API_JSON=credentials.json

4. Add your Google Service Account JSON as credentials.json in project root.


5. Run the FastAPI server:



uvicorn backend.app:app --reload

6. Test incoming calls, bookings, and SMS notifications.




---

Project Structure

backend/
├─ routes/       # API routes
├─ services/     # OpenAI, Twilio, Google API services
├─ utils/        # Config and helpers
├─ tests/        # Dummy tests for CI
├─ app.py        # Main FastAPI app
requirements.txt
README.md
.env (not committed)
credentials.json (not committed)


---

CI/CD

GitHub Actions workflow runs on push or pull request.

Lints code with flake8 and runs pytest tests.










