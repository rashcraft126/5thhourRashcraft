#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: Scenario 1

monsterdict= {
    "Zachasourus":{
        "Health":1000,
        "Damage": 25,
        "Element":"fire"
    },
    "Domimomasourus":{
        "Health":1000,
        "Damage":50,
        "Element":"Ice"
    },
    "Gabasourus":{
        "Health":1000,
        "Damage":25,
        "Element":"Water"

    },
    "Chimera":{
        "Health":5000,
        "Damage":25,
        "Element":"Poison, Fire, Electric"

    },
    "Allisorus": {
        "Health": 900,
        "Damage": 75,
        "Element": "Poison, Water, Electric,Ice"

    }
}
print(monsterdict)
print("Here is the monster dictionary before any applied changes.")

newdamageA = input("Enter the new Damage points for Zachasourus")
monsterdict["Zachasourus"]["Damage"]=newdamageA

newdamageB = input("Enter the new Damage points for Domimomasourus")
monsterdict["Domimomasourus"]["Damage"]=newdamageB

newdamageC = input("Enter the new Damage points for Gabasourus")
monsterdict["Gabasourus"]["Damage"]=newdamageC

newdamageD = input("Enter the new Damage points for Chimera")
monsterdict["Chimera"]["Damage"]=newdamageD

newdamageE = input("Enter the new Damage points for Allisorus")
monsterdict["Allisorus"]["Damage"]=newdamageE

print(monsterdict)
print("Here is your new updated version of your monster dictionary.")