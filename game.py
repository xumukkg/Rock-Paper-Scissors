
from random import randint
while True:
    print()
    print('Rock Paper Scissors')
    turn = int(input("Enter your number 1 = rock, 2 = scissors and 3 =  paper: "))
    while turn>3:
        turn = int(input("Enter your number 1 = rock, 2 = scissors and 3 =  paper "))
    comp_turn  = randint(1,3)
    if comp_turn ==1:
        print("Computer turn is rock ")
    elif comp_turn ==2:
        print("Computer turn is scissors ")
    elif comp_turn ==3:
        print("Computer turn is paper ")
    if turn ==1 and comp_turn == 2:
        print("You win")
    elif turn ==2 and comp_turn ==3:
        print("You win")
    elif turn == 3 and comp_turn == 1:
        print("You win")
    elif turn==comp_turn:
        print("draw")
    else:
        print("You lose")
