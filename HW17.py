#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW17
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello world")

#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def heads_or_tails():
    global heads
    global tails
    for i in range(1,101):
     coinflip=random.randint(1,2)

     if coinflip == 1:
        heads += 1
     else:
        tails += 1


#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
heads_or_tails()

#5. Print the final result of heads and tails here
print("This is how many times you flipped heads," , heads)
print("This is how many times you flipped tails," , tails)