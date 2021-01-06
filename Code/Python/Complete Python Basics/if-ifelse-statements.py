# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# A more sophisticated way to verify name and age in a database; using basic if and else statements.
print('Welcome! Please verify your identity.')
print('Please input your name:')
name = input()
print('Please input your age:')
age = int(input())
print('Finally, what is your password?')
password = input()
# The only person allowed is Ruddy the 20 year old programmer that has the password: Eggs and Bacon.
if name == 'Ruddy' and age == 20 and password == 'Eggs and Bacon':
    print('Welcome to your shift Ruddy! Please get to work : )')
elif name == 'Ruddy' and age != 20 and password != 'Eggs and Bacon':
    print('Wrong name, password OR age. Try again')
else:
    print('INTRUDER!')
