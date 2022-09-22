print("""













""")

age = int(input("""Sup, what is your age?
>>> """))

print("")

if age < 16:
    print("You are too young to vote and drive lol")
elif age < 18 and age > 15:
    print("You are too young to vote lol")
elif age < 25 and age > 18:
    print("You can't rent a car lol")
elif age > 24:
    print("You can do whatever you want lol")