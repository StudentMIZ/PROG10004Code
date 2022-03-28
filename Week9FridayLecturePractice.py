import math 

class Athletes:
    KILOGRAM_PER_POUND = 0.45359237
    METERS_PER_INCH = 0.0254

    def __init__(self):
        self._firstName = ""
        self._lastName = ""
        self._height = 0
        self._weight = 0
        self._bmi = math.inf
        self._condition = ""


    def run(self):
        newFirstName = input("Enter the first name of the athlete: ")
        newLastName = input("Enter the last name of the athlete: ")

        self.setFirstName(newFirstName)
        self.setLastName(newLastName)

        weight = float(input("Enter the weight in pounds: "))
        height = float(input("Enter the height in inches: "))

        self.setWeight(weight)
        self.setHeight(height)

        self.computeBmi(weight, height)

    
    def compute
