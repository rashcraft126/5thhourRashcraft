#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sports= {
    "Sports 1": {
        "Name":"Football",
        "Players": "11",
        "Ball": True,
    },
    "Sports 2": {
        "Name": "Soccer",
        "Players": "11",
        "Ball": True,
    },
    "Sports 3": {
        "Name": "VolleyBall",
        "Players": "6",
        "Ball": True,
    }
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sports_function(a,b,c):
    print(a+b+c)

#3. Call the function with arguments here
sports_function(sports["Sports 1"]["Players"], sports["Sports 2"]["Players"], sports["Sports 3"]["Players"])