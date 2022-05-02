import random
user_action = input("Enter a choice of rock, paper, or scissors: ")
possible_action = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_action)
print('You chose ' + user_action + '. Computer chose ' + computer_action + '.')

def apple():
    while True:
        try:
        except ValueError:
            print("You must enter rock, paper, or scissors")
            break   #this stops running try accept function


if user_action.lower() == computer_action:
    print('Both players selected ' + user_action + '. It is a tie.')

elif user_action.lower() == 'rock':
    if computer_action == 'scissors':
        print('Rock smashes scissors. You win')
    else:
        print('Paper covers rock. You lose.')

elif user_action.lower() == 'scissors':
    if computer_action == 'paper':
        print('Scissors cuts the paper. You win')
    else:
        print('Rock smashes scissors. You lose.')

elif user_action.lower() == 'paper':
    if computer_action == 'rock':
        print('Paper covers rock. You win')
    else:
        print('Scissors cut paper. You lose.')

apple()