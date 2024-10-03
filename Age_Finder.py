# Age finder 
bornyear=int(input("Enter your born date"))
currentyear=2024
months=int(input("Enter the your birth month"))
dat=int(input("Enter the day of the birth"))
Year=currentyear-bornyear
days=Year*12

print(f"Your age is: {Year}")
print(f"age in months {Year*12+months}")
print(f"age in days:{days*30+dat}")