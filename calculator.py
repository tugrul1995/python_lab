import math

#this functions are for the math modules in the project tool.

#THIS ADD FUNCTION
def add(x,y):
    return x + y

#THIS SUBTRACT FUNCTION
def subtract(x,y):
    return x - y

#THIS DIVIDE FUNCTION
def divide(x,y):
    return x / y

#THIIS MULTIPLY FUNCTION
def multiply(x,y):
    return x * y

#HERE YOU HAVE YOU SELECTIONS FOR THE USER TO PICK AS A OPERATION....
print("Please Select Which operation You Neeed; ")
print("1-add")
print("2-subtract")
print("3-divide")
print("4-multiply")

#THIS IS WHERE YOU CREATE THE CHOISE FOR THE USER TO PICK WHICH OPERATION THEY WANT...
#USE -CHOISE- THAN CREATE A INPUT FOR THE USER.... TO TAKE THE INPUT FROM THE USER...
choise = input("Enter choice(1,2,3,4):")

#THIS IS THE PART YOU ASK AND CREATE TWO NUMBER ENTER INPUT FOR THE OPERATION....
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

#THIS IS WHERE YOU WILL CREATE AND MAKE THE OPERATIONS WORK - FUNCTION PROPERLY...
#CREATE EACH OPTION WITH EACH OPERATION...
if choise == '1':
   print(number_1,"+",number_2,"=", add(number_1,number_2))

elif choise == '2':
    print(number_1,"-",number_2,"=", subtract(number_1,number_2))

elif choise == '3':
    print(number_1,"/",number_2,"=", divide(number_1,number_2))

elif choise =='4':
    print(number_1,"*",number_2,'=', multiply(number_1,number_2))

else:
    print("INVALID ENTERANCE")
    print("PLEASE ONLY PICK FROM 1 - 4 OPTIONS")
