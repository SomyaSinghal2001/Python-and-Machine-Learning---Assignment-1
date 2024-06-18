# Question 20 - Write a python program that takes a list of numbers and returns their sum. 

def total_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

input_string = input("Please enter the list of numbers you want to add, separated by spaces: ")
number_list = [int(num) for num in input_string.split()]
sum_of_numbers = total_sum(number_list)
print("The sum of these numbers in the list is - ", sum_of_numbers)