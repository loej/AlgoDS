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
        self.brand = brand
        self.maxspeed = maxspeed
        self.color = color

    def printCar(self):
       x = print(self.brand,self.maxspeed,self.color)

class City:

    def __init__(self, type ):
        pass


Mercedes = Car('Mercedes',200,'white')
Mercedes.printCar()