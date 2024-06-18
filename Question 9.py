# Question 9 - Write a python program that checks if a substring is present in a given string. 

string1 = input("Please enter your text - ")
string2 = input("Please enter your text - ")
if string2 in string1:
    print("string 2 is the subset of string 1.")
else:
    print("string 2 is not a subset of string 1.")
print("Thank You!")