import streamlit as st
from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_whatsapp_number = ''  # Replace with your Twilio WhatsApp number

def send_whatsapp_message(sender_number, recipient_number, message_body):
    try:
        # Create Twilio client
        client = Client(account_sid, auth_token)

        # Send WhatsApp message
        message = client.messages.create(
            body=message_body,
            from_=twilio_whatsapp_number,
            to=f'whatsapp:{recipient_number}'
        )

        return f"WhatsApp message sent successfully. SID: {message.sid}"

    except Exception as e:
        return f"Error: {e}"

def main():
    st.title('WhatsApp Automation with Twilio')

    # User input for phone numbers and message
    sender_number = st.text_input('Your Phone Number (in international format, e.g., +1234567890):')
    recipient_number = st.text_input('Recipient\'s Phone Number (in international format):')
    message_body = st.text_area('Message:', 'Hello, this is a Twilio WhatsApp automation test! 🚀')

    if st.button('Send WhatsApp Message'):
        if sender_number and recipient_number and message_body:
            result = send_whatsapp_message(sender_number, recipient_number, message_body)
            st.success(result)
        else:
            st.warning('Please fill in all fields.')

if __name__ == "__main__":
    main()
