import random
from random import choice

options = ["R", "P", "S"]


def rules(player_move, cpu_move):
    if player_move == cpu_move:
        print("Draw")
        run()
    elif player_move == "R":
        if cpu_move == "S":
            print("Player wins!")
        else:
            print("CPU wins!")
    elif player_move == "P":
        if cpu_move == "R":
            print("Player wins!")
        else:
            print("CPU wins")
    elif player_move == "S":
        if cpu_move == "P":
            print("Player wins!")
        else:
            print("CPU wins!")
    else:
        print("Nothing")

def run():
    player_move = input("Please choose an option: ")
    while player_move not in options:
        print("You have chosen a wrong option, pick again")
        player_move = input("Please choose an option: ")
        
    cpu_move = random.choice(options)
    print(f"Player {player_move}: CPU {cpu_move}")
    return rules(player_move, cpu_move)


game = run()
print(game)

