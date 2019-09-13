from asteroid import Asteroid
import random
import time
import datetime

"""
    A class that maintains a list of asteroid objects in the field. 
    It includes methods that can create Asteroids with randomly generated 
    radius, velocity, position and including it to a list.
"""


class Controller:

    def __init__(self):
        """
        Creates a list of Asteroids
        """
        self.asteroids = []

    @staticmethod
    def createRandomAsteroid():
        """
        Instantiates Asteroids
        :return: instantiated Asteroid object
        """
        return Asteroid(Controller.generateRadius(), Controller.generatePosition(), Controller.generateVelocity())

    @staticmethod
    def generateRadius():
        """
        Creates a randomly generated radius within the range of 1 and 4
        :return: an int value
        """
        return random.randint(1, 4)

    @staticmethod
    def generateVelocity():
        """
        Creates a randomly generated velocity within the range of 0 and 5
        :return: a tuple of type ints
        """
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        z = random.randint(0, 5)
        return (x, y, z)

    @staticmethod
    def generatePosition():
        """
        Creates a randomly generated position with each element within the range of 0 and 100
        :return: a list of type ints
        """
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        return [x, y, z]

    def addAsteroid(self):
        """
        Adds the newly created asteroid to the class variable of Controller
        """
        self.asteroids.append(Controller.createRandomAsteroid())

    def simulate(self, seconds):
        """
        Simulates the movement of the asteroids. It will records the position, velocity, timestamp.
        It 
        """
        for x in range(0, seconds):
            start_time = datetime.datetime.now().microsecond / 10 ** 6
            print(f"Start time: {start_time}")
            for y in range(len(self.asteroids)):
                self.asteroids[x].move()
                print(self.asteroids[x])
                end_time = datetime.datetime.now().microsecond / 10 ** 6
                print(f"End time: {end_time}")
                time.sleep(1 - (end_time - start_time))


def main():
    controller = Controller()
    for x in range(1, 101):
        controller.addAsteroid()
    controller.simulate(3)


if __name__ == '__main__':
    main()
