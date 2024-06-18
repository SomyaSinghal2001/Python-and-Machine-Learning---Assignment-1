# Question 3 - Write a python program that calculates the factorial of a given number.

number = int(input("Please enter your number - "))
fact = 1
if number < 0:
    print("The number is negative and negative numbers do not have factorials.")
elif number == 0:
    print("the factorial of zero is 1.")
else:
    for i in range(1, number +1):
        fact = fact*i
    print("The factorial of ", number, " is ", fact)
print("Thank You!")