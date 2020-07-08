# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# You can write your own funcitons. A "mini" program inside a program.

def Hello():
    for i in range(0, 20):
        print('Hello World' + ' ' + str(i))


# This only runs when the function is called.
Hello()

# Without a function defined you would have to copy and paste the code every single time.

# You can call arguments.
# Prints: 6
print(len('string'))


# Prints 11

def addNum(number):
    return number + 1


newNumber = addNum(10)
print(newNumber)

# Since all functions return values, what does the print() function return?

print('Hello')

# It returns Hello, without the parenthesis
# print returns the string as a side affect. It returns None.
# It represents the lack of a value.
None

# Does not print anything. Every function call has a return value.
# Even if a function does not return anything it returns None by default.
spam = print()

# Keyword Arguments: often used for optional arguments to pass to a function call
print('Hello, World.')
print('Hi, Mars.')

# It always prints a new string or indent by default.
# To avoid this add the following:

print('Hello I like', end=' ')
print('wow')

# You can pass multiple arguemnts:
# It automatically adds a single space between them.
print('cat', 'dog', 'mouse', end=' ]')
print('he', 'l', 'l', sep='--')

