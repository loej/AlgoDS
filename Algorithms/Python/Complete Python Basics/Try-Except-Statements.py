# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# An exception means the entire program has crashed.

def div100by(number):
    try:
        num = 100 / number
        print(num)
    except ZeroDivisionError:
        print('Error: Dont divide by 0.')


div100by(200)
div100by(100)
# You can't divide a number by 0.
# There are not longer any very long error messages.
div100by(0)

# Another example:

print('Please dont input a string')
string = input()
try:
    if int(string) < 0:
        print('Thanks!')
    else:
        print('Ok.')
except ValueError:
    print('I told you not to enter a string!')
