# python code goes here
def start():
    """
    Run all program functions
    """
    print("\nWelcome to the Adventure game")
    print("\nYou are standing in a dark room")
    print("There is a door to your left and right, which one do you take(l or r)")

    answer = input(">").lower()

    if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
        bear_room()
    elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
        monster_room()
    else:
    # else call game_over() function with the "reason" argument
        game_over("Don't you know how to type something properly?")


def play_again():
    """
    This function is to ask the player to play again
    """
    print("\nDo you want to play again? (y or n)")
  
    answer = input(">").lower()
    

    if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
      start()
    elif "n" in answer :
    # if player typed "no" or "n" print thank you for playing    
        print("\nThank you for playing")
    else:
    # if user types anything besides "yes" or "y", exit() the program
      exit()


def game_over(reason):
    """
    game_over function accepts an argument called "reason"
    """
  
    print("\n" + reason)
    print("Game Over!")
  
    play_again()
    """
    ask player to play again or not by activating play_again() function
    """

def diamond_room():
    """
    some prompts on what you would do when you enter the diamond_room
    """
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")

  
    answer = input(">")
  
    if answer == "1":
       """
       the player is dead, call game_over() function with the "reason"
       """
       game_over("They were cursed diamonds! , the building collapsed when you touch the diamonds and you die!")
    elif answer == "2":
         """
         the player won the game
         """ 
         print("\nNice, that was a smart move! Congrats you win the game!")
    else:
         """
         call game_over() with "reason"
         """
         game_over("Go and learn how to type a number.")

def monster_room():
    """
     some prompts for when you enter the monster_room also '\n' is to print the line in a new line
     """
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")

  
    answer = input(">")
    """
    takes users input
    """

    if  answer == "1":
        """
         lead him to the diamond_room()
        """
        diamond_room()
    elif answer == "2":
         """
        the player is dead, call game_over() with "reason"
         """ 
         game_over("The monster was hungry, it ate you.")
    else:
        """
        game_over() with "reason"
        """     
        game_over("Go and learn how to type a number.")

def bear_room():
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print("What would you do? (1 or 2)")
    print("1). Take the honey.")
    print("2). Taunt the bear.")

    answer = input(">")

    if answer == "1":
       """
       The player is killed by the bear
       """ 
       game_over("The bear killed you.")
    elif answer == "2":
         """
         lead him to the diamond_room()
         """
         print("\nGood, the bear moved from the door. You can go through it now!")
         diamond_room()
    else:
         """
         else call game_over() function with the "reason" argument
         """
         game_over("Don't you know how to type a number?")
start()  

