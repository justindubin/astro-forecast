import os

from twilio.rest import Client


def text_justin(body_text: str):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=os.getenv('TARGET_PHONE_NUMBER'),
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        body=body_text,
    )
    print(message.sid)


class Messenger:

    def __init__(self):
        pass
