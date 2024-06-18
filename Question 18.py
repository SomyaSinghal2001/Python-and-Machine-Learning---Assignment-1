# Question 18 - Write a python program that checks if two strings are anagrams of each other. 

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

word1 = "listen"
word2 = "silent"
print(f"Are '{word1}' and '{word2}' anagrams? {are_anagrams(word1, word2)}")
print("Thank You!")