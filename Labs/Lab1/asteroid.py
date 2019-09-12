import random
import datetime


class Asteroid:
    radius = 0
    position = {}
    velocity = {}
    startingTimestamp

    def __init__(self, radius, position, velocity, timestamp):
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._timestamp = timestamp

    def getRadius(self):
        return self._radius

    def getPosition(self):
        return self._position

    def getVelocity(self):
        return self._velocity

    def getTimestamp(self):
        return self._timestamp

    def setRadius(self, radius):
        self._radius = radius

    def setPosition(self, position):
        self._position = position

    def setVelocity(self, velocity):
        self._velocity = velocity

    def move():
        for index in position:
            position[index] += velocity[index]
