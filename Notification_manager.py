from otp_generator import OTP_Generator
import os
from twilio.rest import Client

OTP_generator = otp_generator()
PIN = otp_generator.generate_pin()
PW = OTP_generator.generate_password()

print(PW)
print(PIN)

#--------------Twilio setup_____

# account_sid = 'AC6f116151d21a4d82a76413bc5f07b6ca'
# auth_token = 'b498a4bb728a1093d016af30fa804f80'

# api_key = "0d75e43670b2ffca4032c37ae7d31c39"
# #------------------------------------------
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body=f'Your verification code is: {otp}',
#     from_='+447883304338',
#     to='+447478881797'
# )

# print(message.status)




'''
Email sender


my_email = "Opportunityhubzw@Gmail.Com"
password = "vmlvmqygizoyuesv"

receiver = "Email2_Test@Yahoo.Com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiver,
                        msg=f"SUBJECT:One-time-passcode (OTP)\n\nThe OTP for your account is {otp}. Enter it now to continue logging in.")



'''
