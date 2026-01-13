from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

def send_notification(message_content, author, channel):
    body = f"""🚨 Nova mensagem no Discord

👤 De: {author}
📌 Canal: {channel}

💬 {message_content}
"""

    client.messages.create(
        body=body,
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        to=os.getenv("TWILIO_WHATSAPP_TO")
    )
