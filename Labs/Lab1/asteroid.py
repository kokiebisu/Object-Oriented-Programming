import random
import datetime


class Asteroid:
    id = 0
    timestamp = 0

    def __init__(self, radius, position, velocity):
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._id = self.addID()
        self._timestamp = self.addTimestamp()

    @classmethod
    def addID(cls):
        cls.id = cls.id + 1
        return cls.id

    @classmethod
    def addTimestamp(cls):
        cls.timestamp = datetime.datetime.now()
        return cls.timestamp

    def getID(self):
        return self._id

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
        return f"ID: {self.getID()}, Radius:{self.getRadius()}, Position: {self.getPosition()}, Velocity: {self.getVelocity()}, Timestamp: {self.getTimestamp()}"
