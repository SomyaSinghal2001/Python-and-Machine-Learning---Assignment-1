# Question 17 - Write a program in python that converts a given string to title case (first letter of each word capitalized).

lines = []
while True:
    line = input("Please enter your text (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line.title())

print("Your entered lines are:")
for line in lines:
    print(line)
print("Thank You!")