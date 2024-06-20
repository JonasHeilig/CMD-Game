import os
import json
import log_system
from story_functions.tutorial import tutorial


Logger = log_system.Logger()
Logger.start_log()


def start_game():
    print("Welcome Player!")
    if os.path.exists('user'):
        if any(fname.endswith('.json') for fname in os.listdir('user')):
            choice = input("New Game (n) or Return to Game (r)? ").strip().lower()
        else:
            choice = 'n'
    else:
        os.makedirs('user')
        choice = 'n'

    if choice == 'n':
        new_game()
    elif choice == 'r':
        continue_game()
    else:
        print("Incorrect Input")
        start_game()


def new_game():
    name = input("Enter your Player Name: ").strip()
    filename = f'user/{name}.json'
    if os.path.exists(filename):
        print(f"A Player with the name '{name}' already exist. Take an other name.")
        new_game()
    else:
        player_data = {
            'name': name,
            'game_level': 0,
            'coins': 10,
            'character_level': 1,
            'xp': 0
        }
        with open(filename, 'w') as file:
            json.dump(player_data, file)
        print(f"New Game created for {name}!")
        Logger.log(prefix="Account System", message=f"Account {name} has been created.")
        game_loop(player_data)


def continue_game():
    name = input("Enter your Player Name: ").strip()
    filename = f'user/{name}.json'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            player_data = json.load(file)
        print(f"Welcome Back, {name}!")
        Logger.log(prefix="Account System", message=f"Account {name} has been loaded.")
        game_loop(player_data)
    else:
        print(f"No Player with the name '{name}' found.")
        start_game()


def save_game(player_data):
    filename = f'user/{player_data["name"]}.json'
    with open(filename, 'w') as file:
        json.dump(player_data, file)
    Logger.log(prefix="Account System", message=f"Account {player_data['name']} has been saved.")
    print(f"The game for {player_data['name']} has been saved.")


def game_loop(player_data):
    if player_data['game_level'] == 0:
        tutorial(player_data)
        Logger.log_info(f"Player {player_data['name']} has finish the tutorial")
        player_data['game_level'] = 1
    else:
        print(f"Game is running for {player_data['name']}. Your current coins: {player_data['coins']}. Your current Level: {player_data['character_level']}. Your current XP: {player_data['xp']}.")

    while True:
        action = input("Enter your action (exit to quit): ").strip().lower()
        if action == 'exit':
            save_game(player_data)
            break
        elif action == 'help':
            print("Actions: exit, help")


if __name__ == "__main__":
    start_game()
