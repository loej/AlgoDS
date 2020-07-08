# A 'Class' can be reffered to as the blueprint that contains objects.
class Dog:
    # Class Variables
    dogName = 'Charlie'


# The class 'dog' contains the object string of the dog's name.
# To create the object we set it to a variable.
newObject = Dog()
# To create the object string of the name we use the following convention:
# ClassName(dot)variableCall => Dog.dogName.
print(Dog.dogName)


# Let's create a different class.
# Objective: Create a Car class with a nested Class called 'location'.

class Car:

    # Setting Instance Variables => They are an instance inside a method or constructor.
    def __init__(self, location, brand, maxspeed, color):
        self.location = location
        self.brand = brand
        self.maxspeed = maxspeed
        self.color = color

    # Setting a printCar() method to print all the attributes. If we just print from the.
    # constructor class it will print the location of the contructor. Note: Location is excluded.
    def printCar(self):
        print(self.brand, self.maxspeed, self.color)


class City:

    # Setting Instance Variables => Describes the location of where the car is.
    def __init__(self, type, capacity, name):
        self.type = type
        self.capacity = capacity
        self.name = name

    # Defining a method to print all Location details in one line.
    def printCity(self):
        print(self.type, self.capacity, self.name)


class Employee:

    def __init__(self, totalEmployees, pay, name):
        self.name = name
        self.totalEmployees = totalEmployees
        self.pay = pay


# Function in order to sort objects. Return what we want to sort.
def empSort(emp):
    return emp


# Main function.
if __name__ == '__main__':
    # Creating object with types.
    newCity = City('Urban', 100, 'Buisness City')
    # Creating objects with newCity object and print method. Also populated the Car object with types.
    newCar = Car(newCity.printCity(), 'Mercedes', 200, 'brown')
    # Called printing method from newCar.
    newCar.printCar()
    # Printing employee information.
    emp1 = Employee(100, 20, 'John Doe')
    emp2 = Employee(100, 10, 'Not John')
    emp3 = Employee(200, 5, 'Doe Not')
    allEmps = [emp1, emp2, emp3]

    sortedEmp = sorted(allEmps, key=empSort)
    print(sortedEmp)
