question = ["?"]

print("""













""")

print("Put in values for Force, Mass, and Acceleration. Key in a ? for the unknown variable.")

force = str(input("""Force:
>>> """))

print("")

mass = str(input("""Mass:
>>> """))

print("")

acceleration = str(input("""Acceleration:
>>> """))

print("")

if force in question:
    force = str(force)
    mass = float(mass)
    acceleration = float(acceleration)
    force1 = mass * acceleration
    force1 = round(force1, 2)
    print("Force: " + str(force1))
elif mass in question:
    force = float(force)
    mass = str(mass)
    acceleration = float(acceleration)
    mass1 = force / acceleration
    mass1 = round(mass1, 2)
    print("Mass: " + str(mass1))
elif acceleration in question:
    force = float(force)
    mass = float(mass)
    acceleration = str(acceleration)
    acceleration1 = force  / mass
    acceleration1 = round(acceleration1, 1)
    print("Acceleration: " + str(acceleration1))
else:
    print("I don't know what you said! I am shutting down!")