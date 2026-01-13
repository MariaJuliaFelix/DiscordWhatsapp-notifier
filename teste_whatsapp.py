from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

msg = client.messages.create(
    body="🚀 Teste direto do Python",
    from_=os.getenv("TWILIO_WHATSAPP_FROM"),
    to=os.getenv("TWILIO_WHATSAPP_TO")
)

print(msg.sid, msg.status)
