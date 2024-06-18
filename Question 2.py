# Question 2 - Write a program that checks whether a given number is even or odd.

number1 = int(input("Please Enter your Number - "))

remainder = number1 % 2

if remainder == 0:
    print("The Given Number is Even.")
else:
    print("The Given Number is Odd.")

print("ThankYou!")
