import random

def determine_winner_rps(player, pc):
    if pc == player:
        return "Tie!"
    elif ((pc == "rock" and player == "paper") or 
          (pc == "paper" and player == "scissor") or 
          (pc == "scissor" and player == "rock")
          ):
        return "You win."
    else:
        return "You lose."


RPS = ["rock","paper","scissor"]
player_pick = input("Choose: Rock, Paper or Scissor. ").lower()
pc_pick = random.choice(RPS)

if player_pick in RPS:
    print(f"PC chose: {pc_pick}.\n{determine_winner_rps(player_pick, pc_pick)}")
else:
    print("Invalid input. Insert only: Rock, Paper or Scissor.")