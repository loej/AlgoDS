# A 'Class' can be reffered to as the blueprint that contains objects.
class Dog:
    dogName = 'Charlie'

# The class 'dog' contains the object string of the dog's name
# To create the object we set it to a variable
newObject = Dog()
# To create the object string of the name we use the following convention:
# ClassName(dot)variableCall => Dog.dogName
print(Dog.dogName)

# Let's create a different class.

class Car:

    # Setting attributes
    def __init__(self, brand, maxspeed, color):
        self.brand = 'Lexus'
        self.maxspeed = 200
        self.color = 'blue'

    def printCar(self):
        print(self.brand)



