from menu import Menu


def main():
    """
    Creates a tamagotchi and let's the User take care and interact with it.
    """
    Menu.welcome()
    Menu.prompt_user()
    number_input = int(input())
    if number_input == 1:
        Menu.create_tamagochi()
    else:
        print("Sorry to hear that...")
        exit()
    while True:
        Menu.show_options()
        option_input = int(input())
        if option_input == 1:
            Menu.show_status()
        elif option_input == 2:
            print("\nWhich food would you like to give?")
            print("1. Apple")
            print("2. Orange")
            print("3. Kiwi\n")
            food_input = int(input())
            Menu.feed_food(food_input)
        elif option_input == 3:
            Menu.play()
        elif option_input == 4:
            Menu.give_medicine()
        else:
            print("Invalid Input! Try again!")


if __name__ == "__main__":
    main()
