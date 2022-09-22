import random
from random import randint
import time


print("""















""")
while True:
    exit = ["Exit", "exit"]
    random_number = randint(1,10)
    random_number = str(random_number)

    print("")

    guess = input("""Guess the number im thinking of from 1-10 (you can exit the code by saying "exit"):
>>> """)

    if guess == random_number:
        print("")
        print("You were right lol")
        time.sleep(1)
    elif guess in exit:
        print("")
        print("Alright, exiting...")
        time.sleep(1)
        print("")
        time.sleep(1)
        break
    else:
        print("")
        print("no, you were wrong, my number was " +  str(random_number) + ", get noobed")
        time.sleep(1)