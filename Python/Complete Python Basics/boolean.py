# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# Checks Condition statements using !=, ==, >, <, >=, <=, ||.
print(22 == 22)  # True.
print(44 != 44)  # False.
print(42 == '42')  # False.

# True, Float == Regular Operator; if they're the same values.
print(42.0 == 42)

# Basic Truth Tables:

# Using the '&' Operator.
print(True & True)  # True.
print(True & False)  # The rest are false.
print(False & True)
print(False & False)

# Using the 'or' Operator.
print(True or True)  # True except the last statement.
print(True or False)
print(False or True)
print(False or False)

# Simple comparison between ages using '&'.
print('Sample Comparison 1:\n')
skyColor = 'blue'
president = 200
# False.
print(skyColor == 'red' and 20 == president)

# Comparison using 'or'.
print('Sample Comparison 2:\n')
colorOfSky = 'blue'
randomColor = 'tangerine'
x = 10
y = 10
# True.
print(colorOfSky == randomColor or x == y)
