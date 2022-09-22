import time

print("""













""")

print("Hello, Welcome to the BMI Calculator!")

time.sleep(0.7)

print("""---------------------------------------
""")

mass = float(input("""What is your weight in pounds?
>>> """))

print("")

height1 = float(input("""Awesome! What is your height in feet without inches?
>>> """))

height2 = float(input("""Cool! Now what is your height in inches?
>>> """))

height1 = height1*12

height1 = height1 + height2

bmi = (mass*703)/height1**2

time.sleep(0.6)

print("""
---------------------------------------
""")

print("Your BMI is" , f'{bmi:.2f}' , "!")

print("""
---------------------------------------""")
time.sleep(1)