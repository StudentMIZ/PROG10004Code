class Cars:
    #Theses are the class variables
    rimSize = 18
    numTires = 4

    def __init__(self, numDoors, make, operation):
        #These are the instance variables
        self._numDoors = numDoors
        self._make = make
        self._operation = operation
        self._rimSizeCust = self.rimSize + 1

    def switchOff(self, model):
        self._model = model
        if self._operation == "ON":
            self._operation = "OFF"

    def __str__(self):
        #Made so that when using the function print(object), the needed information is printed in string format, rather than the address
        return "Make: {0}, Number of Doors: {1}, Model: {2}".format(self._make, self._numDoors, self._model)

    def getNumDoors(self):
        return self._numDoors

    def setNumDoors(self, newDoors):
        self._numDoors = newDoors





#car1 = Cars(4, "Honda", "ON")
#car1.switchOff()
#print(car1)
#print(car1.rimSize)
#print(car1.numTires)

#car2 = Cars(2, "Toyota", "OFF")
#print(car2)
#print(car2.rimSize)
#print(car2.numTires)

car1 = Cars(4, "Honda", "ON")
car1.switchOff("CIVIC")
print(car1)
print(car1._rimSizeCust)