# Question 11 - Write a python program that generates the first n numbers in the Fibonacci sequence. 

n=int(input("Enter a number: "))
x=0
y=1
z=0 
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
    