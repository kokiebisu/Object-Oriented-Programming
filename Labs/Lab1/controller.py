from asteroid import Asteroid
import random


class Controller:
    def __init__(self):
        self.asteroids = []

    @staticmethod
    def createRandomAsteroid():
        return Asteroid(Controller.generateRadius(), Controller.generatePosition(), Controller.generateVelocity())

    def addAsteroid(self):
        self.asteroids.append(Controller.createRandomAsteroid())

    @staticmethod
    def generateRadius():
        return random.randint(1, 4)

    @staticmethod
    def generateVelocity():
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        z = random.randint(0, 5)
        return (x, y, z)

    @staticmethod
    def generatePosition():
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        return [x, y, z]

    def simulate(self, seconds):
        for x in range(len(self.asteroids)):
            self.asteroids[x].move()
            print(self.asteroids[x])


def main():
    controller = Controller()
    controller.addAsteroid()
    for x in controller.asteroids:
        print(x)
    controller.simulate(2)


main()
