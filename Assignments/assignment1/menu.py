from tamagochi import Tamagochi


class Menu:
    @staticmethod
    def prompt():
        print("Welcome to Tamagochi\n")
        # Check status
        # Check if tamagochi should be alive or not
        if Tamagochi.isAlive:
            print("What would you like to do? \nSelect from the following: 1. Check status \n2.Feed Tamagochi \n3.Play with Tamagochi")
        # Make a tamagochi for the user
        else:
            print("You don't have a tamagochi!")
            createTamagochi()

    @classmethod
    createTamagochi(cls):
        tamagochis = {1: Pikachu, 2: Squirtle, 3:}
    # if (user has tamagochi) {
    #
    # } else:
    # 1. Check status
    # 2. Feed Tamagochi
    # 3. Play with Tamagochi
