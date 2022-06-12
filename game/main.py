import random
while True:
        # accept str from user: Scissors, Rock and  Paper
        user_list = [ "Scissors", "Rock", "Paper" ]
        user_selection = input("Enter a choice (rock, paper, scissors): ")
                # computer selection
        computer_list = [ "scissors", "rock", "paper"]
        computer_selection = random.choice(computer_list)
        print(f"\nyou choose {user_selection},  computer choose {computer_selection}\n")
                #return selections
        if user_selection == computer_selection:
                print(f"you and computer choose {computer_selection}, therefore, it is tie ")
        elif user_selection == "rock" and computer_selection =="scissors":
                print(f"You win! Rock beats Scissors")
        elif user_selection == "paper" and computer_selection == "rock":
                print(f"you Win! Paper beats Rock")
        elif user_selection == "scissors" and computer_selection == "paper":
                print (f"You Win! Scissors beats Paper")
        else :
                print(f"You Lose!")      
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
                break