#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW11

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
a= 0
while a <= 100:
    a += 1
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
        continue
    elif a % 5 == 0:
        print("Buzz")
        continue
    elif a % 3 == 0:
        print("Fizz")
    else:
        print(a)



