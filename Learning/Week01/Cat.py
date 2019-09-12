class Cat:

    num_lives = 9  # class variable

    def __init__(self, name, age, color, type_):
        self._name = name
        self._age = age
        self._color = color
        self._type_ = type_  # Weak internal variable

        # You shouldn't change the variable but if you have to then ok
        # self.__type = type -> Double underscore can make it very strict

    # toString for developer
    def __repr__(self):
        return f"Cat: name: {self._name}, age: {self._age}, color: {self._color}, type: {self._type_}"

    # toString for users
    def __str__(self):
        return f"Hi! My name is {self.name} and I am {self.age} years old!"

    @classmethod
    def change_default_lives(cls, new_lives):
        cls.num_lives = new_lives


felix = Cat("Bob", 14, "Black", "Unknown")
print(felix.__repr__)
print(felix.__str__)


