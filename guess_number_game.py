import random

numberlist = [
"NUMBER 1#",
"NUMBER 2#",
"NUMBER 3#",
"NUMBER 4#",
"NUMBER 5#",
"NUMBER 6#",
"NUMBER 7#",
"NUMBER 8#",
"NUMBER 9#",
"NUMBER 10#",
]

print("Think of a rondom number between 1 to 10!!!")
answer = input("When you do, to let me know please type YES! :")

if answer == "yes":
    x = random.randrange(1,10)
    print(numberlist[x])
