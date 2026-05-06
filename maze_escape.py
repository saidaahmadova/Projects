def show_intro():
    print("Welcome to Maze Escape!")
    print("Find the correct way out of the maze.\n")


def first_choice():
    choice = input("You are at a crossroads. Go left or right? ").lower()

    if choice == "left":
        river_choice()
    else:
        print("You fell into a trap. Game Over.")


def river_choice():
    choice = input("You arrived at a river. Swim or wait? ").lower()

    if choice == "wait":
        door_choice()
    else:
        print("A crocodile attacked you. Game Over.")


def door_choice():
    choice = input(
        "You see 3 doors: red, blue, yellow. Which one? ").lower()

    if choice == "yellow":
        print("Congratulations! You escaped the maze!")
    elif choice == "red":
        print("Fire room! Game Over.")
    elif choice == "blue":
        print("Monster room! Game Over.")
    else:
        print("Wrong door. Game Over.")


play_again = "yes"

while play_again == "yes":
    show_intro()
    first_choice()

    play_again = input(
        "\nDo you want to play again? yes or no: "
    ).lower()

print("Thanks for playing!")