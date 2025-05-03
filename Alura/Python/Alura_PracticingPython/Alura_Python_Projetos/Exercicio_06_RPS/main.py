import random

def determine_winner_rps(player, pc):
    if pc == "rock" and player == "paper":
        return "You win."
    elif pc == "rock" and player == "scissor":
        return "You lose."
    elif pc == "paper" and player == "scissor":
        return "You win."
    elif pc == "paper" and player == "rock":
        return "You lose."
    elif pc == "scissor" and player == "rock":
        return "You win."
    elif pc == "scissor" and player == "paper":
        return "You lose."
    elif pc == player:
        return "Tie!"
    else:
        return "Error"


RPS = ["rock","paper","scissor"]
player_pick = input("Choose: Rock, Paper or Scissor. ").lower()
pc_pick = random.choice(RPS)

if player_pick in RPS:
    print(f"PC chose: {pc_pick}.\n{determine_winner_rps(player_pick, pc_pick)}")
else:
    print("Invalid input. Insert only: Rock, Paper or Scissor.")