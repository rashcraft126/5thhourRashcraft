#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: Scenario 3
import random
from idlelib.configdialog import changes

#Scenario 3:


#they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4



#Party Dictionary Goes Here
partydict= {
    "LaeZel": {
        "Race": "Githyanki",
        "Class": "Fighter",
        "Background": "Soldier",
        "Health": 25,
        "AC": 17,
        "Damage": random.randint (1,6)+ random.randint (1,6) + 3,
        "Attack mod": 7
    },
    "Shadowheart": {
        "Race": "Half-Elf",
        "Class": "Cleric",
        "Background": "Acolyte",
        "Health": 20,
        "AC": 11,
        "Damage":random.randint(1,6)+2,
        "Attack mod": 6
    },
    "Gale": {
        "Race": "Human",
        "Class": "Wizard",
        "Background": "Sage",
        "Health": 20,
        "AC": 12,
        "Damage": random.randint (1,10),
        "Attack mod": 5
    },
    "Astarion": {
        "Race": "High Elf",
        "Class": "Rogue",
        "Background": "Charlatan",
        "Health": 15,
        "AC": 15,
        "Damage": random.randint(1,6)+4,
        "Attack mod": 4
    }
}


#Enemy Dictionary Goes Here
monsterdict = {
    "Zachasourus": {
        "Health": 25,
        "Damage": random.randint (3,8),
        "Element": "fire",
        "Attack mod": 7,
        "AC": 17
    },
    "Domimomasourus": {
        "Health": 15,
        "Damage": random.randint (3,6),
        "Element": "Ice",
        "Attack mod": 6,
        "AC": 14
    },
    "Chimera": {
        "Health": 15,
        "Damage": random.randint (1,20),
        "Element": "Poison, Fire, Electric",
        "Attack mod": 5,
        "AC": 13
    },
    "Allisorus": {
        "Health": 10,
        "Damage": random.randint (5,10),
        "Element": "Poison, Water, Electric,Ice",
        "Attack mod": 4,
        "AC": 10

    }
}


#Combat Code Goes Here
number = random.randint (1,20 ) + partydict["LaeZel"]["Attack mod"]
print("Press ENTER to roll the die to attack enemy")
if input()=='':
    print(number)

if number >= monsterdict["Domimomasourus"]["AC"]:
    monsterdict["Domimomasourus"]["Health"]-= partydict["LaeZel"]["Damage"]
    print("You hit them!")
    if monsterdict["Domimomasourus"]["Health"]<=0:
        print("Enemy has been defeated!"),
    else:
        print("The enemy is still alive!")
else:
    print("Attack has missed the target!")

if monsterdict["Domimomasourus"]["Health"]>0:
    number = random.randint(1,20) + monsterdict["Domimomasourus"]["Attack mod"]
    print("Press ENTER to roll the die to attack player")
    if input() == '':
        print(number)

        if number >= partydict["LaeZel"]["AC"]:
            partydict["LaeZel"]["Health"] -= monsterdict["Domimomasourus"]["Damage"]
            print("You hit them!")
            if partydict["LaeZel"]["Health"] <= 0:
                print("Player has been defeated!"),
            else:
                print("The player is still alive!")
        else:
            print("Attack has missed the target!")
else:
    print("Enemy is dead!")

#Step 1: Copy enemy dictionary from SC1

#Step 2: Copy party dictionary from SC2

#Step 3: Make sure every enemy and party member has health points (fixed)

#Step 4: Make sure every enemy and party member has an attack modifier (fixed)

#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)

#Step 6: Make every enemy and party member has a damage roll (random)

