# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# Exists in the 'global' scope. (Global variable).
x = 100


def example():
    # Exists in the 'local' scope. (Local scope).
    # These variables won't exist after the program terminates.
    x = 100
    print(x)


# both x's are not in the same scope.

# 1. Algorithms in the global scopes cannot use the variables in the local scope.
# 2. However, code in the local scope CAN use the variables from the global scope.
# 3. Algorithms in one's local scope cannot use code in another's local scope.
# 4. Algorithms in one's function local scope cannot use variables in any other local scope.

# This block of code will NOT work:

def FizzBuzz(number):
    x = 10
    print(x)
    if number % 15 == 0:
        print('Fizz')
    elif number % 10 == 0:
        print('Buzz')
    elif number % 5 == 0:
        print('Fizz Buzz')
    else:
        print('Not a Valid Number')


# FizzBuzz(10) [Uncomment this for the exmaple to work]
# print(number) [Uncomment this for the exmaple to work]
print(x)


# This is because 'number' is not being called by FizzBuzz. Also, number x is not in defind in the global scope.

# Another example:
# This code will NOT work because bacon is defined outside of the scope of spam().
def spam():
    bacon = 'eggs'
    print(bacon)


def spam2():
    # Returns 'None'.
    print(bacon)


# This will break the program.
# spam2()

#  This code WILL work because x is in a global scope.
x = ['berry', 'straw', 'hello']


def printFruits():
    print(x)


printFruits()

# This works because both variables are in the same scope.
google = 'twitter'
# Reassigns the variable.
google = 'hello'
print(google)


# sameScope2() being called inside sameScope() won't work because of rule 3.
def sameScope2():
    print1 = 1
    # This part will be destroryed afterwards
    print(print1)


def sameScope():
    print1 = 12
    print1 = 13
    sameScope2()
    sameScope2()
    print(print1)
    print(print1)


sameScope()


# One last example (again).
# This entire code block will NOT work. Even though the
# program executes, referencing rule 3, we know that
# if we call a function from a local scope into another function
# in a different local scope the function will be destroyed.
# e.g. egg() is called inside movies(). However, since eggs() contains
# a variable in the local scope inside another function's local scope it will never
# be called correctly.
def eggs():
    foo = 10
    print(foo)


def movies():
    o = 100
    eggs()
    eggs()
    eggs()
    eggs = 111
    print(eggs)
    eggs()
    print(foo)


# Is a variable inside a function a local or global variable?
# If there is assignment variable inside a function it is considered a local variable. Otherwise,
# it is considered a global variable.
# Example:

def number1():
    # Local variable: it will now read number in the local scope.
    # global number (uncomment after the bottom example)
    number = 100_00_00_0
    # It will always print the number above because it is in its local scope.
    print(number)


number = 100
# Once it arrives here and number1() is called, the local scope is 'destroyed'.
number1()
# This print() function now looks at the GLOBAL scope and print 200.
print(number + number)


# To make a local scope into a gloabl scope you can use the global keyword. Example:

def food():
    global pizza
    pizza = 'good'
    print(pizza)


pizza = 'bad'
food()

# Why? This limits what can be inside a function inside python.
# Functions can act as 'black boxes'.
