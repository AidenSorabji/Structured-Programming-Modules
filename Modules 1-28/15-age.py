print("""













""")

name = str(input("""Sup, what's your name?
>>> """))

print("")

age = float(input("""Sup """ + name + """, what is your age?
>>> """))

print("")

if age < 16:
    print("You cannot drive, " + name )
elif age == 16 and age == 17:
    print("You can drive, but you cannot vote, " + name)
elif age > 17 and age < 25:
    print("You can drive and vote, but you cannot rent a car, " + name)
elif age > 24:
    print("You can do anything that is legal, " + name)
else:
    print("I have no clue what your age is")
    exit()

    