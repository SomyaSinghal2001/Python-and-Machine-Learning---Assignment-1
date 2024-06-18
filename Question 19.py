# Question 19 - Write a python program that removes all punctuation from a given string. 

import string
input_string = input("Please enter a string: ")
translator = str.maketrans('', '', string.punctuation)
clean_string = input_string.translate(translator)
print("String without punctuation:")
print(clean_string)
print("Thank You!")