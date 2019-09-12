from asteroid import Asteroid
import random
import time


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
        for x in range(0, seconds):
            startTime = time.time()
            for y in range(len(self.asteroids)):
                self.asteroids[x].move()
                print(self.asteroids[x])
            endTime = time.time()
            time.sleep(1 - (endTime - startTime))


def main():
    controller = Controller()
    for x in range(1, 5):
        controller.addAsteroid()
    controller.simulate(2)


main()
