#game greeting
print("Lets answer the math # QUESTIONS CORRECT")

#QUESTION NUMBER ONE
print("Question_1")
print("what is the sum of 2 + 2 = ?")
print("a:4")
print("b:6")
print("c:1")
print("d:9")

answer1 = input()

if answer1 == 'a':
    print("Great Job!")
else:
    print("Please Try again")
while answer1 == 'a':
    print("what is the sum of 2 + 2 = ?")
    break

#QUESTION NUMBER ONE
print("Question_2")
print("what is the multiply of 5 x 5 = ?")
print("a:2")
print("b:10")
print("c:25")
print("d:8")

answer2 = input()

if answer2 == 'c':
    print("You are very smart!")
else:
    print("WRONG! Practice multiplying more..")
while answer2 == 'c':
    print("WRONG! ANSWER AGAIN BUT CORRECT...")
    break
