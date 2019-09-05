import math

# This program will prompt two values from the user.
# The program will then add, subtract, multiply, divide
# or return the hypotenuse of the two values


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

    operators = {1: 'Sum', 2: 'Subtract', 3: 'Multiply', 4: 'Divide'}

    if operatorChoice in operators:
        operation = operators[operatorChoice]

        print(operation)
        print("Enter two values")

        a = int(input())
        b = int(input())

        if operation == "Sum":
            print(calculator.Sum(a, b))
        elif operation == "Subtract":
            print("Subtract: ", calculator.Subtract(a, b), "\n")
        elif operation == "Multiply":
            print("Multiply: ", calculator.Multiply(a, b), "\n")
        else:
            print("Divide: ", calculator.Divide(a, b), "\n")
    else:
        print("Invalid Operator Choice")


calculator = MyCalculator()
flag = False
while flag == False:
    main()
    print("\nYou want to End? \nYes \nNo")
    a = input().lower()
    if (a == 'yes'):
        flag = True
