# second version of OOP 

# Class
class DogShop:

    def __init__(self, numberofDogs, priceperDay, foodPerdog, employees):
        self.numberofDogs = numberofDogs
        self.priceperDay = priceperDay
        self.foodPerdog = foodPerdog
        self.employees = employees

# Empty Employees List
employeesList = []
# Makes doggyLand object
doggyLand = DogShop(0, 100, 0, 0)

# Onboards emplyees 
class OnBoard:

    def includeEmplyee(names):
        #Checks if the list is empty
        if not names:
            print("Please enter the name of an employee.")
        employeesList.append(names)

        print('Employee List:' + str(employeesList))
        for i in range(len(employeesList)):
            print(employeesList[i])
            for j in employeesList[i]:
                print(j, end="|")
                print()
        return employeesList


if __name__=="__main__":
    listEmployees = ["hello", "avatar", "aang"]
    OnBoard.includeEmplyee(listEmployees)

