import random
computer_score = 0
player_score = 0

def score_board():
    print(f"computer Score = {computer_score}")
    print(f"player score = {player_score}")


print("---> Welcome to my Rock Paper Scissors Game <---")
while(True):
    print()
    user_move = input("""> 1. Rock 
> 2. Paper
> 3. Scissors
> 4. Quit: --> """)


    computer_move = random.randint(0, 9)
    if computer_move <= 3:
        p2_Move = "Rock"
    elif computer_move > 3 and computer_move <= 6:
        p2_Move = "Paper"
    elif computer_move > 6 and computer_move <= 9:
        p2_Move = "Scissor"


    #for rock
    if user_move == "1":
        if p2_Move == "Rock":
            print(f"You choose Rock and computer choose {p2_Move} You tied")
            score_board()
        elif p2_Move == "Paper":
            print(f"You choose Rock and computer choose {p2_Move} Computer Wins")
            computer_score += 1
            score_board()    
        elif p2_Move == "Scissors":
            print(f"You choose Rock and computer choose {p2_Move} You Win")
            player_score += 1
            score_board()

    #for paper
    elif user_move == "2":
        if p2_Move == "Rock":
            print(f"You choose Paper and computer choose {p2_Move} You win")
            player_score += 1
            score_board()
        elif p2_Move == "Paper":
            print(f"You choose Paper and computer choose {p2_Move} tied")
            score_board()
        elif p2_Move == "Scissors":
            print(f"You choose Paper and computer choose {p2_Move} Computer wins")
            computer_score += 1
            score_board()

    #for Scissos
    elif user_move == "3":
        if p2_Move == "Rock":
            print(f"You choose Scissors and computer choose {p2_Move} Computer wins")
            computer_score += 1
            score_board()
        elif p2_Move == "Paper":
            print(f"You choose Scissors and computer choose {p2_Move} You win")
            player_score += 1
            score_board()
        elif p2_Move == "Scissors":
            print(f"You choose Scissors and computer choose {p2_Move} tied")
            score_board()

    elif user_move == "4":
        print("GoodBye!")
        break