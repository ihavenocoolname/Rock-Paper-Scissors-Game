import random

rock = "rock"
paper = "paper"
scissors = "scissors"


#R,P & S are assigned a number 1-3
#randomly selects a number 1-3 and prints corresponding hand
#this way, each time I call throw(), the roll is re-randomized

def throw():
    print("Your turn! rock, paper or scissors?")
    user_throw = input()

    

    hand = random.randint(1,3)

    if hand == 1:
        print(rock)
    elif hand == 2:
        print(paper)
    else:
        print(scissors)
    



throw()
throw()
throw()
throw()




