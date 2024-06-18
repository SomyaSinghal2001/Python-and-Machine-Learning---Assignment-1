# Question 13 - Write a program that asks the user for their birth year and calculates their age. 

import datetime
current_year = datetime.datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("Your age is - ", age)
print("Thank You!")