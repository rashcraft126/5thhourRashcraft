#Name: Ryley Ashcraft
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

numofplayers= int(input("Enter the amount of players"))
sum = 0
i = 0
print("Lets rate their outfits")
while i < numofplayers:
    i += 1
    rating = int(input("Enter the rating from 1-5 for player"))
    if rating > 5 or rating < 1:
        i -= 1
        print("Error")
        continue
    else: sum = sum + rating

print ("The average rating for the players is", sum / numofplayers)









