print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input('You are at a crossroad. Type "left" or "right": ').lower()

if choice1 == "left":

    choice2 = input('You arrived at a lake. Type "wait" or "swim": ').lower()

    if choice2 == "wait":

        choice3 = input(
            'There are 3 doors: Red, Blue, Yellow. Which one? ').lower()

        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Wrong door. Game Over.")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")