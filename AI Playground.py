#Name: Ryley Ashcraft
'''''
import random
import time


def slow_print(text):
    """Function to print text slowly for effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


def intro():
    slow_print("You wake up in a dimly lit room. The air smells musty, and you feel uneasy.")
    slow_print("You are in an old, creaky house. The floorboards groan as you move.")
    slow_print("A sudden gust of wind blows open the door, and you hear faint whispers from the hallway.")
    slow_print("Do you dare to explore the house or stay put and wait for help?")

    choice = input("Type 'explore' to go down the hallway or 'stay' to wait. ").lower()

    if choice == 'explore':
        hallway()
    elif choice == 'stay':
        slow_print("You stay still, hoping for help. Suddenly, the whispers get louder, and the door slams shut.")
        game_over()
    else:
        slow_print("Invalid choice, try again!")
        intro()


def hallway():
    slow_print(
        "You cautiously step into the hallway. The air is colder now, and your breath is visible in the dim light.")
    slow_print("A door creaks open to your left, and you hear someone crying. The house seems alive with sound.")
    slow_print("You feel the presence of something watching you.")

    choice = input("Do you approach the door or continue down the hallway? (Type 'approach' or 'continue') ").lower()

    if choice == 'approach':
        creepy_room()
    elif choice == 'continue':
        dark_room()
    else:
        slow_print("Invalid choice, try again!")
        hallway()


def creepy_room():
    slow_print(
        "You open the door slowly. Inside, you see a dark figure standing in the corner, its back turned to you.")
    slow_print("Suddenly, it turns around, and its face is a grotesque mask of twisted features.")
    slow_print("It lunges at you, and you feel a chill run down your spine as you realize you are trapped!")

    # Random chance of survival
    outcome = random.choice([True, False])
    if outcome:
        slow_print("You manage to escape the room, but you hear footsteps behind you!")
        hallway()  # Player goes back to the hallway
    else:
        slow_print("The figure grabs you, and everything goes black. Game over.")
        game_over()


def dark_room():
    slow_print("You enter the dark room. It is pitch black, and you can barely see your hand in front of you.")
    slow_print("Suddenly, the door slams shut behind you! You feel around for a way out.")
    slow_print("You hear a soft scratching noise from the corner of the room.")

    choice = input(
        "Do you try to find a light switch or search for a way to open the door? (Type 'light' or 'search') ").lower()

    if choice == 'light':
        light_switch()
    elif choice == 'search':
        search_room()
    else:
        slow_print("Invalid choice, try again!")
        dark_room()


def light_switch():
    slow_print("You feel around the wall and finally find the light switch.")
    slow_print("You flip the switch, and the room is illuminated.")
    slow_print("The walls are covered in strange symbols, and the air smells of decay.")

    slow_print("You hear something move in the corner.")
    slow_print("It's a small creature, but its eyes glow red. It stares at you with hatred.")

    # Random outcome
    outcome = random.choice([True, False])
    if outcome:
        slow_print("You quickly grab a nearby chair and throw it at the creature, buying yourself time to escape.")
        hallway()  # You get back to the hallway
    else:
        slow_print("The creature lunges at you with terrifying speed and you can't escape.")
        game_over()


def search_room():
    slow_print("You feel around in the dark, knocking over a few items.")
    slow_print("Your hand brushes something cold and metallic.")
    slow_print("You pull it closer to find a bloody knife!")
    slow_print("Suddenly, you hear breathing behind you. It's too late to react.")

    game_over()


def game_over():
    slow_print("GAME OVER")
    choice = input("Would you like to play again? (yes/no): ").lower()
    if choice == 'yes':
        intro()
    else:
        slow_print("Thanks for playing!")
        exit()


# Start the game
intro()
'''''
'''''
import random
import time


def slow_print(text):
    """Function to print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


def intro():
    slow_print("You wake up in a dark, cold room. Your head aches, and you have no idea how you got here.")
    slow_print("The room is silent, but you can feel something is wrong. There's a faint smell of mildew in the air.")
    slow_print("Suddenly, you hear the creaking of the door. Someone or something is watching you.")
    slow_print("You must escape, but there's no time to waste. You need to act quickly!")

    choice = input("Do you want to look around the room or try the door? (Type 'look' or 'door') ").lower()
    if choice == 'look':
        look_around()
    elif choice == 'door':
        try_door()
    else:
        slow_print("Invalid choice. Try again.")
        intro()


def look_around():
    slow_print("You look around the room. The walls are damp, and the air is heavy.")
    slow_print("There's a small desk in the corner, and a shelf above it filled with dusty books.")
    slow_print("You also notice a small window, but it's too high to reach. The door seems to be the only exit.")

    choice = input("Do you want to search the desk or try the door? (Type 'desk' or 'door') ").lower()
    if choice == 'desk':
        desk_search()
    elif choice == 'door':
        try_door()
    else:
        slow_print("Invalid choice. Try again.")
        look_around()


def desk_search():
    slow_print(
        "You open the desk drawer. Inside, you find a flashlight and a piece of paper with strange symbols written on it.")
    slow_print("The flashlight flickers to life, but it feels like it's about to die any second.")
    slow_print(
        "You take the paper, and a sudden chill runs down your spine. The paper seems to be a clue, but it’s unclear what it means.")

    choice = input("Do you want to keep searching or try the door? (Type 'search' or 'door') ").lower()
    if choice == 'search':
        random_event()  # Stalker event happens here.
    elif choice == 'door':
        try_door()
    else:
        slow_print("Invalid choice. Try again.")
        desk_search()


def random_event():
    # Randomly decides if the stalker has found you
    outcome = random.choice([True, False])
    if outcome:
        slow_print("You hear the faintest sound—a footstep behind you!")
        stalker_encounter()
    else:
        slow_print("You continue searching, but you find nothing else of interest.")
        look_around()


def stalker_encounter():
    slow_print("A cold hand grabs your shoulder. You freeze in fear.")
    slow_print("A voice whispers in your ear: 'You're not leaving this place.'")
    slow_print("The room grows colder, and you feel the presence of the stalker closing in.")

    choice = input("Do you try to break free or scream for help? (Type 'break' or 'scream') ").lower()
    if choice == 'break':
        break_free()
    elif choice == 'scream':
        scream_for_help()
    else:
        slow_print("Invalid choice. Try again.")
        stalker_encounter()


def break_free():
    slow_print("You muster all your strength and push the hand away, breaking free from the stalker's grip.")
    slow_print("You rush to the door, but it’s locked! You’re trapped.")
    slow_print("The stalker laughs softly from behind you. There's no time left.")
    game_over()


def scream_for_help():
    slow_print("You scream for help, but no one answers. The room seems to swallow your voice.")
    slow_print("The stalker steps closer, their breath cold on your neck.")
    slow_print("They whisper, 'You won't make it out alive.'")
    slow_print("The room begins to fade away, and everything goes black.")
    game_over()


def try_door():
    slow_print("You try the door, but it’s locked. You need to find a key or some other way out.")
    slow_print("You feel the hairs on the back of your neck stand up. The stalker is near.")
    slow_print("A cold gust of wind blows from under the door, and you hear a soft whisper.")

    choice = input("Do you want to search the room again or try the window? (Type 'search' or 'window') ").lower()
    if choice == 'search':
        desk_search()  # Can find more clues.
    elif choice == 'window':
        try_window()
    else:
        slow_print("Invalid choice. Try again.")
        try_door()


def try_window():
    slow_print("You try to reach the window, but it’s too high up. You need something to climb on.")
    slow_print("You notice a nearby chair that could help you reach it, but you hear footsteps approaching.")
    slow_print("The stalker is getting closer!")

    choice = input("Do you use the chair to climb or stay put? (Type 'climb' or 'stay') ").lower()
    if choice == 'climb':
        climb_window()
    elif choice == 'stay':
        slow_print("You stay put, hoping the stalker won't find you. But it's too late.")
        game_over()
    else:
        slow_print("Invalid choice. Try again.")
        try_window()


def climb_window():
    slow_print("You manage to climb the chair and reach the window. It creaks open with difficulty.")
    slow_print("As you slip through the window, you hear the stalker screaming in anger.")
    slow_print("You’ve escaped... for now.")
    slow_print("But you know they’ll be watching.")
    game_win()


def game_over():
    slow_print("GAME OVER. You didn't make it out in time.")
    choice = input("Do you want to try again? (yes/no): ").lower()
    if choice == 'yes':
        intro()
    else:
        slow_print("Thanks for playing! Goodbye.")
        exit()


def game_win():
    slow_print("CONGRATULATIONS! You managed to escape the haunted room!")
    choice = input("Would you like to play again? (yes/no): ").lower()
    if choice == 'yes':
        intro()
    else:
        slow_print("Thanks for playing! Stay safe.")
        exit()


# Start the game
intro()
'''''
'''''
import random
import time

def slow_print(text):
    """Function to print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def display_instructions():
    slow_print("""
    Welcome to the Basketball Roulette Game!
    In this game, you'll bet on basketball events and spin the roulette wheel to see the outcome.
    The roulette wheel has the following events:

    1. Make a Shot - You score a basket!
    2. Miss a Shot - You miss the basket.
    3. Get a Rebound - You grab a rebound.
    4. Steal the Ball - You steal the ball from your opponent.
    5. Turnover - You lose possession of the ball.
    6. Foul - You commit a foul.

    You can bet on one of the above events. Let's see if luck is on your side!
    """)

def spin_roulette():
    """Function to simulate spinning the roulette and getting a random event."""
    events = [
        "Make a Shot",
        "Miss a Shot",
        "Get a Rebound",
        "Steal the Ball",
        "Turnover",
        "Foul"
    ]
    return random.choice(events)

def place_bet():
    """Function to allow the player to place a bet on one of the events."""
    slow_print("Place your bet on one of the following events:")
    slow_print("1. Make a Shot")
    slow_print("2. Miss a Shot")
    slow_print("3. Get a Rebound")
    slow_print("4. Steal the Ball")
    slow_print("5. Turnover")
    slow_print("6. Foul")

    bet_choice = input("Enter the number of the event you want to bet on (1-6): ")

    if bet_choice == '1':
        return "Make a Shot"
    elif bet_choice == '2':
        return "Miss a Shot"
    elif bet_choice == '3':
        return "Get a Rebound"
    elif bet_choice == '4':
        return "Steal the Ball"
    elif bet_choice == '5':
        return "Turnover"
    elif bet_choice == '6':
        return "Foul"
    else:
        slow_print("Invalid choice. Please select a number between 1 and 6.")
        return place_bet()  # Recursively call to re-enter the bet.

def play_round():
    """Function to handle one round of the basketball roulette."""
    bet = place_bet()  # Let the player place a bet
    slow_print("Spinning the roulette...")
    time.sleep(1)  # Simulate the spinning
    result = spin_roulette()  # Spin the roulette wheel

    slow_print(f"The result is: {result}!\n")

    if bet == result:
        slow_print("Congratulations! You win this round!")
    else:
        slow_print("Sorry, you lost this round. Better luck next time.")

def play_game():
    """Main function to run the game."""
    slow_print("Welcome to the Basketball Roulette Game!\n")
    display_instructions()

    while True:
        play_round()

        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice != 'yes':
            slow_print("Thanks for playing Basketball Roulette! Goodbye!")
            break

# Start the game
play_game()
'''''
