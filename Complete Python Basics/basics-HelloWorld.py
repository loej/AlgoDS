# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# Prints 'Hello World'.
print('Hello, World.')

# Asks for any name and outputs the name.
print('What is your name?')
x = input()
print('Nice to meet you ' + x + '.')

# Prints the length of name.
print('The length of your name is:')
print(len(x))

# Asks a for age and calculates the age a year later.
g = input('What is your age? \n')
print('Your age is: ' + g + '.')
print('You will be: ' + str(int(g) + 1) + ' in one year.')
