import math

"""
    A program that will prompt two values from the user.
   The program will then add, subtract, multiply, divide
   or return the hypotenuse of the two values
"""


class MyCalculator:
    def CalculateHypotenuse(a, b):
        return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    def Sum(self, a, b):
        return a + b

    def Multiply(self, a, b):
        return a * b

    def Divide(self, a, b):
        return a / b

    def Subtract(self, a, b):
        return a - b


def main():

    print("\n\n### Welcome to the Calculator ###")
    print("\nWhich operator do you want to use?")
    print("1. Sum \n2. Subtract \n3. Multiply \n4. Divide \n")

    operatorChoice = int(input())

    print("\nYou are ready for Calculating...")

    if operatorChoice in operators:
        operation = operators[operatorChoice]

        print(operation)

        a = int(input("Enter the first value"))
        b = int(input("Enter the second value"))

        # if operation == "Sum":
        #     print("Sum: ", calculator.Sum(a, b))
        # elif operation == "Subtract":
        #     print("Subtract: ", calculator.Subtract(a, b), "\n")
        # elif operation == "Multiply":
        #     print("Multiply: ", calculator.Multiply(a, b), "\n")
        # else:
        #     print("Divide: ", calculator.Divide(a, b), "\n")

        operators = {1: calculator.Sum(a, b), 2: calculator.Subtract(
            a, b), 3: calculator.Multiply(a, b), 4: calculator.Divide(a, b)}
        result = operators[operatorChoice]
        print("Result: {}".format(result))
    else:
        print("Invalid Operator Choice")


if __name__ == "__main__":
    calculator = MyCalculator()
    flag = False
    while flag == False:
        main()
        print("\nYou want to End? \nYes \nNo")
        a = input().lower()
        if (a == 'yes'):
            flag = True
