#Name: Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW5

#1. Print "Hello World!"
print("Hello world!")

#2. Create a list that contains 3 integers
numblist=[12,5,18]

#3. Create an if statement that prints out whichever of the three numbers is the highest
if numblist[0]>numblist[1] and numblist[0]>numblist[2]:
    print("The biggest number is,",numblist[0])
else:
    print(numblist[0], "Is not the greatest number.")

if numblist[1]>numblist[2] and numblist[1]>numblist[2]:
    print("The biggest number is,",numblist[1])
else:
    print(numblist[1], "Is not the greatest number.")

if numblist[2]>numblist[1] and numblist[2]>numblist[0]:
    print("The biggest number is,",numblist[2])
else:
    print(numblist[2], "Is not the greatest number.")