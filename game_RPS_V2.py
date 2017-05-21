# I'm sure there are more efficient ways to code this.
#Especially regarding informing player of computer's throw
#The WIN/LOSE conditions could have been more efficiently programmed

#Still, this is much more concise and logical than my first attempt.

#we'll need a way to randomize the computer's throws. Done with random
from random import randint

#computer will randomly select one element from the list
throw = ["Rock", "Paper", "Scissors"]
computer = throw[randint(0,2)]


#while player is false, game will loop. Once player enters input, player is no longer false
player = False
while player == False:
    player = input("Rock, Paper, or Scissors?")
#if/else statements determine the outcome of each game, and inform player    
    if player == computer:
        print("Tie!")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer selected " + str(computer) + ". computer covers player. You lose, buddy!")
        elif computer == "Scissors":
                  print("Computer selected " + str(computer) + ". Player smashes scissors. You win!")
        
    elif player == "Paper":
            if computer == "Scissors":
                print("Computer selected " + str(computer) + ". Computer cuts player. You lose, pal!")
            elif computer == "Rock":
                print("Computer selected " + str(computer) + ". Player covers computer. You win!")

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer selected " + str(computer) + ". Computer smashes player. You lose, mate!")
        elif computer == "Paper":
            print("Computer selected " + str(computer) + ". Player cuts computer. You win!")
    else:
        print("Invalid throw. Check spelling & capitalization")
#reset player to false so the above while loop continues to run
    player = False
#re-randomize the computer's roll. Otherwise, it will continue with the first roll selected
    computer = throw[randint(0,2)]
