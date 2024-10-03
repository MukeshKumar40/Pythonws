import random

# Function to generate a 6-digit OTP
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

print("Your 6-digit OTP is:", generate_otp())