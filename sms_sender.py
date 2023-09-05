from number_generator import Number_Generator
import os
from twilio.rest import Client

num_generator = Number_Generator()
otp = int(num_generator.otp)
print(otp)

#--------------Twilio setup_____

account_sid = 'AC6f116151d21a4d82a76413bc5f07b6ca'
auth_token = 'b498a4bb728a1093d016af30fa804f80'

api_key = "0d75e43670b2ffca4032c37ae7d31c39"
#------------------------------------------
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f'Your verification code is: {otp}',
    from_='+447883304338',
    to='+447478881797'
)

print(message.status)
