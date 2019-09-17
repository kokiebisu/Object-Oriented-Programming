# from tamagochi import Tamagochi
# import datetime


# class Pikachu(Tamagochi):
#     """
#     Pikachu is a specialied tamagotchi.
#     """
#     amount = 2
#     rate = 1
#     happiness_amount = 40
#     hunger_base_amount = 60
#     pikachu_sick = 60
#     pikachu_happinessAmount = 1
#     preferred_food = {"Apple", "Orange"}
#     playlist = ["You played a game with Pikachu",
#                 "You did hide and seek with Pikachu",
#                 "You played soccer with Pikachu"]

#     def __init__(self, health=100, happiness=100, hunger=0, is_alive=True, last_checked=0):
#         """
#         Initialize a pikachu object with a default health, happiness count of 100, hunger of 0 and a isAlive state of True
#         :param health: an int
#         :param happiness: an int
#         :param hunger: an int
#         :param is_alive: a boolean
#         :param last_checked: a datetime objecy
#         """
#         super().__init__(
#             health, happiness, hunger, is_alive)

#     def decrease_health(self, time):
#         """
#         Overrides the tamagotchi's decrease_health function with pikachu's own unique speed of decreasing.
#         :param time: an int
#         """
#         super().decrease_health(self.amount, time)

#     def decrease_happiness(self, time):
#         """
#         Overrides the tamagotchi's decrease_happiness function with pikachu's own unique speed of decreasing
#         :param time: an int
#         """
#         super().decrease_happiness(self.amount, time)

#     def increase_hunger(self, time):
#         """
#         Overrides the tamagotchi's increase_hunger function with pikachu's own uniqued speed of increasing
#         :param time: an int
#         """
#         super().increase_hunger(self.amount, time)

#     def give_food(self, food):
#         """
#         Overrides the tamagotchi's give_food function with pikachu's own unique amount of decreasing hunge
#         :param food: an int
#         """
#         super().give_food(food, self.preferred_food, self.hunger_base_amount)

#     def play(self, play_input):
#         """
#         Overrides the tamagotchi's play function with pikachu's own unique amount of increasing happiness
#         :param playInput: an int
#         """
#         super().play(self.playlist[play_input], self.happiness_amount)

#     def update_status(self):
#         """
#         Overrides the tamagotchi's update_status function with pikachu's unique way of decreasing the
#         health, happiness and increasing hunge
#         """
#         time_elapsed = datetime.datetime.now() - self._last_checked
#         time_elapsed_in_seconds = time_elapsed.total_seconds()
#         self._time_elapsed = time_elapsed
#         self.decrease_health(time_elapsed_in_seconds)
#         self.decrease_happiness(time_elapsed_in_seconds)
#         self.increase_hunger(time_elapsed_in_seconds)
#         self._last_checked = datetime.datetime.now()

#     def is_sick(self):
#         """
#         Overrides the tamagotchi's is_sick function with pikachu's standard value of getting sick
#         """
#         super().is_sick(self.pikachu_sick)

#     def __str__(self):
#         """
#         Overriden to print the pikchu's attributes
#         """
#         return f"\nPikachu: health: {round(self._health)}, happiness: {round(self._happiness)}, hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}\n"
