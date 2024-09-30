#Name:
#Class: 5th Hour
#Assignment: HW6
#Link=https://www.tutorialspoint.com/python/nested_if_statements_in_python.htm#:~:text=Example%20of%20Nested%20if%20Statement&text=num%20%3D%2036%20print%20(%22num,ends....%22)&text=num%20%3D%2036%20Divisible%20by%203%20and%202%20....
import random

#Objectives

#1. Print Hello World!
print("Hello World")
#2. Create a variable named num and assign it a variable.
num = random.randint(1,100)
print("Your random number is", num)
#3. Create a nested if statement follows this structure:
if num % 2 == 0:
    if num % 3 == 0:
        print("The result of", num, "being divided by 2 is", num/2)
        print("The result of" ,num/2,"being divided by 3 is",num/2/3)
    else:
        print("Your number is not divisible by 3")
        print("The result of", num, "being divided by 2 is", num / 2)
elif num % 3 == 0:
        print("the num is not divisible by 2")
        print("The result of", num, "being divided by 3 is", num / 3)
else:
    print("Your number is not divisible by 2 or 3")