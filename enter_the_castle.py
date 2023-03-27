##enter_the_castle
#mr_lees
#20/03/23

#use import to load the random library
import random

#Introduce the adventure
print("You are in a dark room in a mysterious castle.")
print("In front of you are four doors. You must choose one.")

#Adding a loop to our code 
repeat = True
while repeat is True:
    #get the player to choose option 1, 2, 3 or 4
    player_choice = int(input("Choose 1, 2, 3, or 4..."))

    if player_choice <= 0 or player_choice >= 5:
        print("Sorry you didn't enter 1, 2, 3 or 4.")
        print("Run the game again to have another go.")
#breaks the loop
    else:
        repeat = False 
    
#add 3 player choices to navigate the castle using conditions

player_choice = random.randint(1,10)

#20% chance of getting number 1
if player_choice >= 1 and player_choice <= 2:
    print("You find a room full of treasure. You're rich!")
    print("GAME OVER, YOU WIN!")

#20% chance of getting number 2
elif player_choice >= 3 and player_choice <= 4:
    print("The door opens and an angry ogre hits you with his club.")
    print("GAME OVER, YOU LOSE..")

#40% chance of getting number 3
elif player_choice >= 5 and player_choice <= 8:
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragons gold.")
    print("2) Try to sneak around the dragon to the exit.")
    dragon_choice = int(input("Type 1 or 2..."))
    if dragon_choice == 1:
        print("The dragon wakes up and eats you! NOM NOM NOM!!")
        print("GAME OVER, YOU LOSE!")
    elif dragon_choice == 2:
        print("You sneak around the dragon and escape the castle, blinking in the sunshine.")
        print("GAME OVER, YOU WIN!")
    else:
        print("Sorry, you didn't enter 1 or 2.")

        
#20% chance of getting number 4
elif player_choice >= 9 and player_choice <= 10:
    print("You enter a room with a sphinx")
    print("It asks you to guess what number it is thinking of, between 1 and 10.")
    number = int(input("What number do you choose?"))


    if number == random.randint(1,10):
        print("The sphinx hisses in disappointment. You guessed correctly")
        print("She must let you go free")
        print("GAME OVER. YOU WIN!")

    else:
        print("The sphinx tells you that your guess is incorrect.")
        print("You are now her prisoner forever.")
        print("GAME OVER. YOU LOSE!")

