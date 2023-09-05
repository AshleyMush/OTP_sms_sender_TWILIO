import string
import random



class OTP_Generator:
    '''
    returns a random int or random string object
    '''
    def __init__(self):
        self.otp_pin = ''
        self.otp_pw = ''

    def generate_pin(self,length= 6):
        '''This will return the pin as a string, convert result to int'''
        characters = string.digits  # Use only digits
        for _ in range(length):
            self.otp_pin += random.choice(characters)
        return int(self.otp_pin)
    
    def generate_password(self,length =16):
        characters = string.ascii_letters #use letters only
        for _ in range(length):
            self.otp_pw += random.choice(characters)

        return self.otp_pw


