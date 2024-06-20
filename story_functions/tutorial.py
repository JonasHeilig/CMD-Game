import time


def tutorial(player_data):
    print(f"Hello, {player_data['name']}! Welcome to the Game Tutorial.")
    input("Press Enter to continue... ")
    print("Story telling...")
    time.sleep(3)
    print("Story telling...")
    time.sleep(3)
    print("Story telling...")
    time.sleep(3)
    print("Story telling...")
    time.sleep(3)
    while True:
        print("Are you ready to start the game?")
        action = input("When you are ready type yes: ").strip().lower()
        if action == 'yes':
            print("Great! Let's start the game.")
            print(
                f"Hello {player_data['name']}! Your current coins: {player_data['coins']}. Your current Level: {player_data['character_level']}.  Your current XP: {player_data['xp']}.")
            break
