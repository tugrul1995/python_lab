import random

# The Jokes I picked
jokeslist = [
    "What did the man say to his fingers? I’m counting on you.",
    "How does the ocean say hello? It waves.",
    "How do pigs do their homework? With a pigpen.",
    "How do you hire a horse? Put it on a ladder.",
    "How do you fix a broken tomato? With tomato paste."
]

print("Can I make a good joke for you ?")

answer = input("Type your answer: ")

if answer == "yes":
    x = random.randrange(0,4)
    print(jokeslist[x])
else:
    print("ok, get off my sight!!!")
