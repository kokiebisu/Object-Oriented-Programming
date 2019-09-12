class Temperature:

    def __init__(self, fahrenheit):
        self.temp = fahrenheit

    def _get_temp(self):
        return f"{str(self.temp)} F"

    def _set_temp(self, fahrenheit):
        if fahrenheit > 0:
            self.temp = fahrenheit

    @classmethod
    def _get_responses(self):
        return ["This is the class method of Temperature"]

# Always add a underscore inside properties


classroom_temp = Temperature(60)
print(classroom_temp._get_temp())
print(classroom_temp._get_responses())
