#Name:
#Class: 5th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
a = 1
while a <=30:
    a+=1
    if a % 2 == 0:
        print(a)

#3. Create a while loop that repeats until the user
#inputs the number 0.
print("Try and guess the correct number")
k = int(input())

while k != 0:
    if k == 0:
        break
    k = int(input("Wrong number!"))




