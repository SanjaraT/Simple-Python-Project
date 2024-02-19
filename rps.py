import random
print(" WELCOME TO THE GAME!")
print("---------------------")
options = ["rock","paper","scissors"]
user_wins =0
comp_wins =0
while True:
    user_pick = input("PLEASE ENTER ROCK/PAPER/SCISSORS OR Q TO QUIT: ").lower()
    if user_pick == "q":
        break
    elif user_pick not in options:
        print("INVALID")
        continue
    random_num = random.randint(0,2)
    computer_pick = options[random_num]
    print("COMPUTER PICKED: ",computer_pick +"!")

    if user_pick == "rock" and computer_pick == "scissors":
        print("YOU WON!")
        user_wins +=1
    elif user_pick == "paper" and computer_pick == "rock":
        print("YOU WON!")
        user_wins += 1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("YOU WON!")
        user_wins += 1
    else:
        print("YOU LOST!")
        comp_wins +=1

    print("YOU WON",user_wins,"times.")
    print("COMPUTER WON",comp_wins,"times.")
print("GOODBYE!")