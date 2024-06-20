import os
import json


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
            'level': 1,
            'score': 0
        }
        with open(filename, 'w') as file:
            json.dump(player_data, file)
        print(f"New Game created for {name}!")
        game_loop(player_data)


def continue_game():
    name = input("Enter your Player Name: ").strip()
    filename = f'user/{name}.json'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            player_data = json.load(file)
        print(f"Welcome Back, {name}!")
        game_loop(player_data)
    else:
        print(f"No Player with the name '{name}' found.")
        start_game()


def game_loop(player_data):
    print(player_data)


if __name__ == "__main__":
    start_game()
