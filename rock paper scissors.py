import random

def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors): ")
    opions = ["rock","paper", "scissors"]
    computer_choice = random.choice(opions)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors! you win!"
        else:
            return "paper covers rock! you lose"
        
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cuts paper! you lose."
        
    elif player == "scissors":
        if computer == "paper":
            return "scissors cover paper! you win!"
        else:
            return "rock smashes scissors! you lose."
    
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
