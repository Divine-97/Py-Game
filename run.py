# python code goes here
def start():
    print("\n You are standing in a dark room")
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

def bear_room():
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print("What would you do? (1 or 2)")
    print("1). Take the honey.")
    print("2). Taunt the bear.")

    answer = input(">")

    if answer == "1":
    # the player is dead!
        game_over("The bear killed you.")
    elif answer == "2":
    # lead him to the diamond_room()
        print("\nYour Good time, the bear moved from the door. You can go through it now!")
        diamond_room()
    else:
    # else call game_over() function with the "reason" argument
        game_over("Don't you know how to type a number?")
start()  

