import time

print("""













""")

print("Hello, Welcome to the BMI Calculator!")

time.sleep(0.7)

print("""---------------------------------------
""")

mass = float(input("""What is your weight in kilograms?
>>> """))

print("")

height = float(input("""Awesome! What is your height in meters?
>>> """))

bmi = mass/(height)**2

time.sleep(0.6)

print("""
---------------------------------------
""")

print("Your BMI is" , f'{bmi:.2f}' , "!")

print("""
---------------------------------------""")
time.sleep(1)