import time


def tutorial(player_data):
    print(f"Hello, {player_data['name']}! Welcome to the Game Tutorial.")
    input("Press Enter to continue... ")
    print("Hello Player! Welcome to the Game Tutorial. I will guide you through the game.")
    time.sleep(5)
    print("The game is simple. It is a little text-based Sandbox Game.")
    time.sleep(5)
    print("You can go mine for resources, chop wood, fight monsters, and level up your character.")
    time.sleep(5)
    print("To start with, you have 10 coins, and you are at Level 1.")
    time.sleep(5)
    print("But first, let's start with the basics.")
    while True:
        print("Are you ready to start the game?")
        time.sleep(5)
        action = input("When you are ready type yes: ").strip().lower()
        if action == 'yes':
            print("Great! Let's start the game.")
            break
        elif action == 'no':
            print("Okay! Take your time. When you are ready, type yes.")
        elif action == 'exit':
            print("You can't exit the tutorial. You need to finish it.")
        elif action == 'help':
            print("Type 'yes' to go on with the tutorial.")
        elif action == '-cheat-leavetutorial-':
            print(
                f"Hello {player_data['name']}! Your current coins: {player_data['coins']}. Your current Level: {player_data['character_level']}. Your current XP: {player_data['xp']}.")
            return
    time.sleep(5)
    print("There is a simple command that helps you always. It is the 'help' command.")
    time.sleep(5)
    print("You can use the 'help' command to get a list of all available actions.")
    time.sleep(5)
    print("Now, let's start with the first action. Type 'help' to know what to do.")

    while True:
        action = input("Enter your action: ").strip().lower()
        if action == 'help':
            print("Great! You can use the 'help' command to know what to do.")
            time.sleep(5)
            print("To exit the Tutorial dialog and go into the interactive part of the tutorial in Map, type 'exit'.")
            time.sleep(7)
            break
        elif action == 'exit':
            print("You can't exit the tutorial. You need to finish it.")

    while True:
        action = input("Enter your action: ").strip().lower()
        if action == 'exit':
            print("Great! You have learned two commands: 'help' and 'exit'.")
            time.sleep(5)
            print("When you use the 'exit' command now, it will save your game and exit it.")
            time.sleep(5)
            print("But now, let's go to the interactive part of the tutorial.")
            time.sleep(5)
            print(
                f"Hello {player_data['name']}! Your current coins: {player_data['coins']}. Your current Level: {player_data['character_level']}. Your current XP: {player_data['xp']}.")
            time.sleep(5)
            print("Now, let's learn how to mine resources.")
            time.sleep(5)
            print("Type 'mine' to mine for resources.")

            while True:
                action = input("Enter your action: ").strip().lower()
                if action == 'mine':
                    print("Great! You mined some resources.")
                    time.sleep(5)
                    print("Now, let's learn how to chop wood.")
                    break
                elif action == 'help':
                    print("Type 'mine' to mine for resources.")
                else:
                    print("Unknown action! Type 'help' for a list of available actions.")

            print("Type 'chop' to chop wood.")

            while True:
                action = input("Enter your action: ").strip().lower()
                if action == 'chop':
                    print("Great! You chopped some wood.")
                    time.sleep(5)
                    print("You have completed the tutorial!")
                    break
                elif action == 'help':
                    print("Type 'chop' to chop wood.")
                else:
                    print("Unknown action! Type 'help' for a list of available actions.")
            break
        elif action == 'help':
            print("Great! You can use the 'help' command to know what to do.")
            time.sleep(5)
            print("To exit the Tutorial dialog and go into the interactive part of the tutorial in Map, type 'exit'.")
            time.sleep(5)
