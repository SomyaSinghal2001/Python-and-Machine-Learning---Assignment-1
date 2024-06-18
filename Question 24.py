# Question 24 - Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

def calculator(num1, num2):
    operator = input("Enter operator (+, -, *, /) - ")
    if operator == "+" :
        print("the sum of the numbers is - ", num1 + num2)
    elif operator == "-" :
        print("the difference of the numbers is - ", num1 - num2)
    elif operator == "*" :
        print("the product of the numbers is - ", num1 * num2)
    else:
        print("the quotient of the numbers is - ", num1 / num2)
        
num1 = int(input("Enter your first number - "))
num2 = int(input("ENter your second number - "))
calculator(num1, num2)
print("Thank You!")