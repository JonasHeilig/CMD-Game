import os
import json
import log_system
from story_functions.tutorial import tutorial
import random

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
    print("To Create a new Game, please enter your Player Name.")
    name = input("Enter your Player Name: ").strip()
    filename = f'user/{name}.json'
    if os.path.exists(filename):
        print(f"A Player with the name '{name}' already exists. Choose another name.")
        new_game()
    else:
        player_data = {
            'name': name,
            'game_level': 0,
            'coins': 10,
            'character_level': 1,
            'xp': 0,
            'inventory': {
                'wood': 0,
                'stone': 0,
                'coal': 0,
                'iron': 0,
                'gold': 0,
                'diamond': 0
            }
        }
        with open(filename, 'w') as file:
            json.dump(player_data, file)
        print(f"New Game created for {name}!")
        Logger.log(prefix="Account System", message=f"Account {name} has been created.")
        game_loop(player_data)


def continue_game():
    print("To continue your Game, please enter your Player Name.")
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


def game_loop(player_data):
    if player_data['game_level'] == 0:
        tutorial(player_data)
        Logger.log_info(f"Player {player_data['name']} has finished the tutorial")
        player_data['game_level'] = 1
        player_data['inventory']['wood'] += 10
        player_data['inventory']['stone'] += 4
        player_data['inventory']['iron'] += 1
        print("You received 10 wood, 4 stone, and 1 iron for completing the tutorial!")
        Logger.log_info(f"{player_data['name']} received 10 wood, 4 stone, and 1 iron for completing the tutorial.")
        save_game(player_data)
    else:
        print(
            f"Game is running for {player_data['name']}. Your current coins: {player_data['coins']}. Your current Level: {player_data['character_level']}. Your current XP: {player_data['xp']}.")

    while True:
        action = input("Enter your action: ").strip().lower()
        if action == 'exit':
            save_game(player_data)
            break
        elif action == 'help':
            print("Actions: mine, chop, exit, inventory, help")
        elif action == 'mine':
            mine(player_data)
        elif action == 'chop':
            chop_wood(player_data)
        elif action == 'inventory':
            print_inventory(player_data)
        else:
            print("Unknown action! Type 'help' for a list of available actions.")


def save_game(player_data):
    filename = f'user/{player_data["name"]}.json'
    with open(filename, 'w') as file:
        json.dump(player_data, file)
    Logger.log(prefix="Account System", message=f"Account {player_data['name']} has been saved.")
    print(f"The game for {player_data['name']} has been saved.")


def mine(player_data):
    with open('settings.json', 'r') as file:
        settings = json.load(file)
    ores = settings["ores"]
    ore = random.choices(list(ores.keys()), list(ores.values()))[0]
    player_data['inventory'][ore] += 1
    Logger.log_info(f"{player_data['name']} mined {ore}. Current {ore} count: {player_data['inventory'][ore]}.")
    print(f"You mined some {ore}. You now have {player_data['inventory'][ore]} {ore}(s).")


def chop_wood(player_data):
    with open('settings.json', 'r') as file:
        settings = json.load(file)
    trees = settings["trees"]
    tree = random.choices(list(trees.keys()), [trees[t]["probability"] for t in trees])[0]
    wood_amount = trees[tree]["wood_amount"]
    player_data['inventory']['wood'] += wood_amount
    Logger.log_info(
        f"{player_data['name']} chopped down a {tree} tree and got {wood_amount} wood. Current wood count: {player_data['inventory']['wood']}.")
    print(
        f"You chopped down a {tree} tree and got {wood_amount} wood. You now have {player_data['inventory']['wood']} wood.")


def print_inventory(player_data):
    print("Inventory:")
    for item, amount in player_data['inventory'].items():
        print(f"{item.capitalize()}: {amount}")


if __name__ == "__main__":
    start_game()
