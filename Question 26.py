# Question 26 - Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 

input_string = input("Please enter your text - ")
prefix = input("Enter the prefix to check - ")
suffix = input("enter the suffix to ckeck - ")

if input_string.startswith(prefix):
    print("Entered text starts with the given prefix!")
else:
    print("Entered text does not start with the given prefix!")
    
if input_string.endswith(suffix):
    print("Entered text ends with the given suffix!")
else:
    print("Entered text does not end with the given suffix!")
print("Thank You!")
