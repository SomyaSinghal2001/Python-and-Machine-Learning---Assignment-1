# Question 23 - Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 

def function(num):
    choice = input("you want to convert into celsius or fahrenheit? (c/f) - ")
    if choice == "f":
        result = num * 9 / 5 + 32
        print("Temperature in fahrenheit is - ", result)
    elif choice == "c":
        result = (num - 32) * 5 / 9
        print("Temperature in celsius is - ", result)
    else:
        print("Not Valid")
num = int(input("Enter number - "))
function(num)
print("Thank You!")