import random

#Starting values
text = "Guess a number (1 - 100): "
correct = False
guesses = 0
#Randomized number
random_n = random.randint(1,99)

def check_guess(random_n, player_n):
    if player_n == random_n:
        return True, f"Correct! You guessed the right number, {random_n}"
    elif player_n > random_n:
        return False, "Too high, the number is smaller. Try again: "
    else:
        return False, "Too low, the number is bigger. Try again: "

def player_guess(text):
    try:
        player_n = int(input(text))
        if 1 <= player_n <= 100:
            return player_n
        else:
            return player_guess("Number outrside range! Try again, Insert a number between 1 and 100: ")
    except:
            return player_guess("Invalid input! Insert only whole numbers: ")

while not correct:
    guesses += 1
    player_n = player_guess(text)
    correct, text = check_guess(random_n,player_n)
    if correct:
        print(text, f"in {guesses} guesses.")
