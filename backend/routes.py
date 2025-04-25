# backend/routes.py
from fastapi import APIRouter, HTTPException
from twilio_fallback import send_fallback_sms

rcs_router = APIRouter()

@rcs_router.post("/send")
def send_message(to: str, message: str, rcs_supported: bool):
    if rcs_supported:
        return {"status": "RCS message sent (mock)", "to": to, "message": message}
    else:
        success = send_fallback_sms(to, message)
        if success:
            return {"status": "SMS fallback sent", "to": to}
        raise HTTPException(status_code=500, detail="Failed to send SMS fallback")
@rcs_router.get("/status")
def get_status():
    # This is a placeholder for the actual status check
    return {"status": "RCS service is running", "version": "1.0"}
@rcs_router.get("/health")
def health_check():
    # This is a placeholder for the actual health check
    return {"status": "healthy", "version": "1.0"}