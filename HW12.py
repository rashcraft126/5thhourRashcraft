#Name: Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW12
import time

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.

for i in range (5, 0, -1):
    time.sleep(0.4)
    print(i)
else:
    print("Hello World")

#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)

for a in range(1,31):
    if a % 2 == 0:
        print(a)

#3. Create a for loop that prints 5 different animals from a list.
animals = ["Lion", "Gazelle", "Rabbit", "Wolf", "Snake"]
for y in animals:
    print(y)

#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for w in input()[::-1]:
    print(w)