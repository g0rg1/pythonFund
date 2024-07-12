import random 


coloda = [6,7,8,9,10,11,12]
player_points = random.randint(coloda[0] , coloda[6])
diller_points = random.randint(coloda[0] , coloda[6])

print(f"Your start points are {player_points}")
print(f"Diller start points are{diller_points}")





while True:
    print("Do you want to take a card?")
    answer = input("y/n?")
    if answer == "y":
        player_points += random.randint(coloda[0] , coloda[6])
        print(f"Your new points are {player_points}")
        print ("Do you want to add a diller card?")
        d_answer = input("y/n?")
        if d_answer == "y":
            diller_points += random.randint(coloda[0] , coloda[6])
            print(f"Diller points are {diller_points}")
        else: 
            break
    else:
       break
   
if player_points >21 or diller_points>21:
    print("You have too much , you loose")
elif player_points > diller_points:
    print("Player wins")
elif player_points < diller_points:
    print("Diller wins")
elif player_points == diller_points :
    print("Draw")

   