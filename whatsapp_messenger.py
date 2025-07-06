import os
from twilio.rest import Client

def send_whatsapp(message):
    try:
        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+27789258901'
        )
        return f"✅ WhatsApp message sent. SID: {message.sid}"
    except Exception as e:
        return f"❌ Failed to send WhatsApp: {e}"
