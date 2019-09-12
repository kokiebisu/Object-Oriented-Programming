import random
import datetime


class Asteroid:

    def __init__(self, radius, position, velocity):
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._id = self._id + 1

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

    def move(self):
        for index in range(len(self._position)):
            self._position[index] = self._position[index] + \
                self._velocity[index]

    def __str__(self):
        return f"Radius:{self._radius}, Position: {self._position}, Velocity: {self._velocity}, Timestamp: {self._velocity}, Id: {self._id}"
