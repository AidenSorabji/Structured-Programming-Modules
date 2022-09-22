print("""


















""")

import time

count_start = input("""Count from:
>>> """)

print("")

count_to = input("""Count to:
>>> """)

count_to = int(count_to)

count_to = count_to + 1

print("")

count_by = input("""Count By:
>>> """)

print("""
-------------
""")

time.sleep(1)

count_start = int(count_start)
count_to = int(count_to)
count_by = int(count_by)

print("""Alright, here you go:
""")

for number in range(count_start,count_to,count_by):
    print(number)