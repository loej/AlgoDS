# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# Prints 'Hello World' 5 iterations.
spam = 1
while spam < 5:
    print('Hello, World.')
    spam += 1
else:
    print('The value is not less than 5.')

# Keeps asking four string until it equals the String (Input Validation).
name = ''
while name != 'Joel':
    print('Please type in your name:')
    name = input()
print('Thank you!')

# Uses Break statement.
name = ''
while True:
    print('Please type your name:')
    name = input()
    if name == 'Joel':
        # Immediately jumps out of loop.
        break
print('Thanks!')

# Uses Continue statement, jumps back to the while loop and reevaluates execution.
spam = 0
while (spam < 5):
    spam += 1
    if (spam == 2):
        # Immediatley jumps back to the loop and skips the print statement.
        continue
    print('The spam is:' + str(spam))

# Printing a Star Triangle using a while loop.
triangleStars = int(input('Enter the number of rows:'))
row = 0
while row < triangleStars:
    # We want each star to correspond to their index number + 1.
    star = row + 1
    # Prints the star. Each star is printed as long as its  greater than 0. Subtracts the amount after each print.
    while star > 0:
        print('*', end=' ')
        star -= 1
    # Increments each row.
    row += 1
    print()

# Prints upside down triangle.
howManyStars = int(input("Enter the number of rows:"))
i = 0
while i < howManyStars:
    c = howManyStars
    while (c > i):
        c = c - 1
        print('*', end=' ')
    i = i + 1
    print()

# Full Triangle.

configureNumber = int(input("How many stars do you want?: "))

rows = 0
# Main constraint.
while rows < configureNumber:
    # We need to print a star and space.
    space = configureNumber - rows - 1
    # 0 is the boundry
    while space > 0:
        print(end=" ")
        # We want it to terminate using -1, space = 3 => 3 -1 => space = 2 => 2-1 => space = 1 etc.
        space -= 1
    # print star.
    star = rows + 1
    while star > 0:
        print("*", end=" ")
        # We want end to be in the same line.
        star -= 1
        # we need to continue the other half.
    # we need to increment row value.
    rows += 1
    print()
