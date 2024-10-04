#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW7
from operator import truediv

#1. Print Hello World!
print("Hello World")

#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = False
admin = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
users = 14
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
            users += 1
            print("Welcome, User. You have logged in", users," times")
        else:
            print("You are missing your admin")
    else:
        print("You are missing your login")
else:
    print("You are missing your wifi connection")
