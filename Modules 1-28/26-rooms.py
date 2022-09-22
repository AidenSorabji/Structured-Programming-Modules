import time

up = ["Up", "up", "U", "u"]
down = ["Down", "down", "D", "d"]
left = ["Left", "left", "L", "l"]
right = ["Right", "right", "R", "r"]

while True:
    room1 = input("""You are in room, you have to find right room.

controls: up = u, down = d, left = l, right = r

X = you are here
----------------------------
|       3|       6|       9|
|        |        |        |
|        |        |        |
----------------------------
|       2|       5|       8|
|        |        |        |
|        |        |        |
----------------------------
|       1|       4|       7|
|    x   |        |        |
|        |        |        |
----------------------------

>>> """)
    if room1 in up:
        room2 = input("""You are in room, you have to find right room.

controls: up = u, down = d, left = l, right = r

X = you are here
----------------------------
|       3|       6|       9|
|        |        |        |
|        |        |        |
----------------------------
|       2|       5|       8|
|    x   |        |        |
|        |        |        |
----------------------------
|       1|       4|       7|
|        |        |        |
|        |        |        |
----------------------------

>>> """)
        if room2 in up:
            print("""you win, pog

here is map of where win is
----------------------------
|       3|       6|       9|
|    x   |        |        |
|        |        |        |
----------------------------
|       2|       5|       8|
|        |        |        |
|        |        |        |
----------------------------
|       1|       4|       7|
|        |        |        |
|        |        |        |
----------------------------
""")
            time.sleep(1)
            exit()
        elif room2 in right:
            room5 = input("""you die, you bad at game
----------------------------
|       3|       6|       9|
|        |        |        |
|        |        |        |
----------------------------
|       2|       5|       8|
|        |    x   |        |
|        |        |        |
----------------------------
|       1|       4|       7|
|        |        |        |
|        |        |        |
----------------------------
""")
            time.sleep(1)
            exit()

    elif room1 in right:
        room4 = input("""you die, you bad at game
----------------------------
|       3|       6|       9|
|        |        |        |
|        |        |        |
----------------------------
|       2|       5|       8|
|        |        |        |
|        |        |        |
----------------------------
|       1|       4|       7|
|        |    x   |        |
|        |        |        |
----------------------------
""")
        time.sleep(1)
        exit()
