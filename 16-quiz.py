from re import A
import time

# Classify
yes = ["YES", "Yes", "yes", "Y", "y"]
no = ["NO", "No", "no", "N", "n"]
false = ["FALSE", "False", "false", "F", "f"]
true = ["TRUE", "True", "true", "T", "t"]
a = ["A", "a"]
b = ["B", "b"]
c = ["C", "c"]
hamburger = ["Hamburger", "hamburger"]

# Set points
points = 0

print("""













""")

# Start quiz
start_quiz = input("""Do you wanna start the quiz? (Y/N)
>>> """)

if start_quiz in yes:
    print("")
elif start_quiz in no:
    print("")
    print("Alright, exiting quiz")
    time.sleep(1)
    exit()
else:
    print("")
    print("No clue what you are trying to say, so I'm shutting down.")
    exit()

time.sleep(1)

print("""---------------------------------
""")

# 1st Question:
our_teacher = input("""1. Who is our teacher?
  A. Mr. Mathews
  B. Mr. John
  C. Ms. McEvoy

>>> """)

print("")

if our_teacher in a:
    print("You are correct! You earn a point!")
    points = points + 1
    print("")
elif our_teacher in b:
    print("Im sorry, you are not correct!")
    print("")
elif our_teacher in c:
    print("Im sorry, you are not correct!")
    print("")

time.sleep(1)

print("""---------------------------------
""")

# 2nd Question:
learning_code = input("""2. We are learning to code Java
   True
   False

>>> """)

print("")

if learning_code in true:
    print("Im sorry, you are not correct!")
elif learning_code in false:
    print("You are correct, you get a point!")
    points = points + 1
else:
    print("Im sorry, you are not correct1")

print("")

time.sleep(1)

print("""---------------------------------
""")

# 3rd Question:
do_good_school = input("""3. You are suppose to do good in school
   True
   False
   Hamburger

>>> """)

print("")

if do_good_school in true:
    print("You are correct! You get a point!")
    points = points + 1
elif do_good_school in false:
    print("You are wrong! (of course you are suppose to do good in school)")
elif do_good_school in hamburger:
    print("You are wrong lol, hamburgers have nothing to do with school")
else:
    print("I have no clue what you said, but it wasn't the answer, so you are wrong!")

print("")

time.sleep(2)

# Ending total & percentage
print("""---------------------------------
""")

if points == 3:
    print("You got 3/3! That is 100%! Congrats!")
elif points < 3:
    percentage_end = (points / 3) * 100
    percentage_end = str(round(percentage_end, 2))
    print("You got " + str(points) + "/3! That is " + str(percentage_end) + "%!")
else:
    breakpoint

print("""
---------------------------------""")
time.sleep(3)