import string
import random
class Number_Generator:
    def __init__(self):
        # self.random_number =

        self.otp = self.generate_otp()

    def generate_otp(self,length= 6):
        characters = string.digits  # Use only digits
        otp = ''
        for _ in range(length):
            otp += random.choice(characters)
        return otp

