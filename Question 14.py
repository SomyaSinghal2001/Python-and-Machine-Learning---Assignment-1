# Question 14 - Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. 

lines = []

while True:
    line = input("Please enter your text (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

print("Your entered lines are:")
for line in lines:
    print(line)
