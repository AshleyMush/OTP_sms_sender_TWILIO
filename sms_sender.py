from number_generator import Number_Generator
import os
from twilio.rest import Client

num_generator = Number_Generator()
otp = int(num_generator.otp)
print(otp)

#--------------Twilio setup_____

account_sid = 'YOUR SID'
auth_token = 'YOUR TOKEN'

api_key = "YOUR KEY"
#------------------------------------------
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f'Your verification code is: {otp}',
    from_='YOUR NUM',
    to='RECEIVER NUM'
)

print(message.status)
