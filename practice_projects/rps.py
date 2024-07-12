import random 

user_choice = input("Выберите жест")

possible_choice = ["Rock" , "Paper" , "Scissors"]

bot_choice = random.choice(possible_choice)

if user_choice == bot_choice:
    print("Draw")
elif user_choice == "Rock":
    if bot_choice == "Paper":
        print("You loose")
    elif bot_choice == "Scissors":
        print("You win")
        
elif user_choice == "Paper":
    if bot_choice == "Rock":
        print("You win")
    elif bot_choice == "Scissors":
        print("You loose")
        
elif user_choice == "Scissors":
    if bot_choice == "Rock":
        print("You loose")
    elif bot_choice == "Paper":
        print("You win")
