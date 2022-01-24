import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type in please Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input=='q':
        break

    if(user_input not in options):
        print('This is not a valid entry\n')
        continue

    r=random.randint(0,2)
    # rock = 0 paper = 1 scissors = 2
    computer_pick = options[r]
    print("The computer picked",computer_pick+'.')

    if user_input == computer_pick:
        print("It's a draw, play again \nThe score is\n",'You:',user_score,"\nComputer's Score:",computer_score)
        continue

    elif user_input == 'rock' and computer_pick == 'scissors':
        user_score += 1
        print("You got it champ this round \nThe score is\n",'You:',user_score,"\nComputer's Score:",computer_score)

    elif user_input =='paper' and computer_pick == 'rock' :
        user_score += 1
        print("You got it champ this round \nThe score is\nYou:",user_score,"\nComputer's Score:",computer_score)

    elif user_input == 'scissors' and computer_pick == 'paper':
        user_score += 1
        print("You got it champ this round \nThe score is\n",'You:',user_score,"\nComputer's Score:",computer_score)


    else:
        computer_score += 1
        print("The computer got you this time \nThe score is\n",'You:',user_score,"\nComputer's Score:",computer_score)


print ("Goodbye")
