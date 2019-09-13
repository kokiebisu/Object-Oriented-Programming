import random
import datetime

"""
This is a class that instantiates a Asteroid object. It
will contain the properties: radius in meters, position and 
velocity uses x, y, z indexes
"""


class Asteroid:
    id = 0

    def __init__(self, radius, position, velocity):
        """
        Initializes the properties of Asteroid
        :param radius: A value of type int
        :param position: A list consisted of 3 elements (x, y, z)
        :param velocity: A tuple consisted of 3 elements (x, y, z)
        """

        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._id = self.addID()
        self._timestamp = self.addTimestamp()

    @classmethod
    def addID(cls):
        """
        Adds a unique id as the property of the instance
        :return: Unique id of type int
        """
        cls.id = cls.id + 1
        return cls.id

    @classmethod
    def addTimestamp(cls):
        """
        Adds a time stamp property to the instance
        :return: the timestamp that was created at the moment of the call of the method
        """
        cls.timestamp = datetime.datetime.now()
        return cls.timestamp

    def getID(self):
        """
        Gets the ID
        :return: an int value
        """
        return self._id

    def getRadius(self):
        """
        Gets the radius in meters
        :return: an int value
        """
        return self._radius

    def getPosition(self):
        """
        Gets the position as a list of three elements x, y, z
        :return: list of ints
        """
        return self._position

    def getVelocity(self):
        """
        Gets the velocity as a tuple of three elements x, y, z
        :return: tuple of ints
        """
        return self._velocity

    def getTimestamp(self):
        """
        Gets the timestamp property of the instance
        :return: a string value
        """
        return self._timestamp

    def setRadius(self, radius):
        """
        Sets the radius of type int
        :param radius: an int value
        :return: an int value
        """
        self._radius = radius

    def setPosition(self, position):
        """
        Sets the position of the Asteroid
        :param position: an int value
        :return: a list of ints
        """
        self._position = position

    def setVelocity(self, velocity):
        """
        Sets the velocity of the Asteroid
        :param velocity: an int value
        :return: an int value
        """
        self._velocity = velocity

    def move(self):
        """
        Moves the position of the Asteroid based on the velocity
        """
        for index in range(len(self._position)):
            self._position[index] = self._position[index] + \
                self._velocity[index]

    def __str__(self):
        """
        Prints a string on the console to display properties when initialized
        :return: A string value
        """
        return f"ID: {self.getID()}, Radius:{self.getRadius()}, Position: {self.getPosition()}, Velocity: {self.getVelocity()}, Timestamp: {self.getTimestamp()}"
