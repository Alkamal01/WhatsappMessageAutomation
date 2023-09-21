from twilio.rest import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

from_number = "your_twilio_phone_number"

to_number = "recipient_whatsapp_number"

# Message content
message_text = "Hello, this is an automated WhatsApp message!"

try:
    # Send the WhatsApp message
    message = client.messages.create(
        body=message_text,
        from_=from_number,
        to=to_number
    )
    print("WhatsApp message sent successfully.")
except Exception as e:
    print(f"Error sending WhatsApp message: {str(e)}")
