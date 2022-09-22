from random import randint
import time

exit = ["Exit", "exit"]
enter = ["""
"""]

print("""















""")

while True:
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    dice3 = randint(1,)

    dice1 = str(dice1)
    dice2 = str(dice2)

    print("Rolling two dice...")
    time.sleep(2)

    print("""
---------------------
    """)

    print("""You have Rolled:""")
    print("")
    print("Dice 1 = " + str(dice1))
    print("")
    print("Dice 2 = " + str(dice2))

    print("""
---------------------
    """)

    time.sleep(2)

    restart = input("""Press Enter to Restart (or type exit to exit out of program
>>> """)

    if restart in exit:
        exit()
    
    elif restart in enter:
        print("""
    ---------------------
        """)
