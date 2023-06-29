
import random

print("roll dices?")
answer = input("yes or no : ")

if answer == "yes":
    x = random.randrange(1,6)
    print(x)

    b = random.randrange(1,6)
    print(b)

elif answer == "no":
    print("Thank you for your time!")
