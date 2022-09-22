import random
from random import randint
import time


print("""















""")
while True:
    exit = ["Exit", "exit"]
    random_number = randint(1,10)
    random_number = str(random_number)
    while True:
        print("")

        guess = input("""Guess the number im thinking of from 1-10 (you can exit the code by saying "exit"):
>>> """)

        if guess == random_number:
            print("")
            print("you right you win bruh")
            time.sleep(1)

            exit()
        elif guess in exit:
            print("")
            print("Alright, exiting...")
            print("")
            time.sleep(1)
            exit()
        else:
            print("")
            if guess > random_number:
                print("no, number too high you guess")
            elif guess < random_number:
                print("no, number too low, guess better")
            time.sleep(1)