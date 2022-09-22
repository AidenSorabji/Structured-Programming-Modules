from time import time


import time

print("""













""")

user_age_years = input("""What is your age?
>>> """)

print()

time.sleep(0.6)

user_age_years = int(user_age_years)

print("You are" , user_age_years , "years old? Wow!")

user_age_years = user_age_years * 365

time.sleep(1.5)

print("You are also" , user_age_years , "days old!")

user_age_years = (user_age_years / 365.25) * 8760

time.sleep(1.5)

print("Did you know you are also" , f'{user_age_years:.2f}' , "hours old!")

user_age_years = (user_age_years / 8760) * 525600

time.sleep(1.5)

print("Also, you are" , f'{user_age_years:.2f}' , "minutes old!")

user_age_years = (user_age_years / 525600) * 31556952

time.sleep(1.5)

print("Fun fact, you are" , f'{user_age_years:.2f}' , "seconds old!")

time.sleep(2)

print("""
Wow, you are old!""")