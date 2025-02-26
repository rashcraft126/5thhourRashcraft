#Name: Ryley Ashcraft
#Class: 5th hour
#Assignment:Playground

def name_print():
    print("Hello there, what is your name?")
    name=input()
    print("Wonderful name,", name)
    print("Now give me 3 other names")
    Name1=input()
    Name2=input()
    Name3=input()
    namelist=[Name1,Name2,Name3]
    print(namelist)

def numbers():
    print("Now lets do some math. Pick 5 numbers between 1-100")
    x=numb1=int(input())
    y=numb2=int(input())
    a=numb3=int(input())
    b=numb4=int(input())
    c=numb5=int(input())
    numblist= [numb1,numb2,numb3,numb4,numb5]
    print(numblist)
    print("Theres your numbers. Now lets add", numb2, "and", numb5, ".")
    sum= y+c
    print(sum)

name_print()
numbers()
