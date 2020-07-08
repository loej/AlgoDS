# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/

# Standard Library and modules:

import random

# Passes a random integer between 1 and 10.
# You need the module name when calling it.
print(random.randint(1, 10))

# An example of importing multiple libraries.
import sys, os, math

# You can also import everything from a standard library.
from sys import *
# The * shows it is an import of everything

# Another example:

from random import *

# Instead of typing RANDOM.randint you can just type randint(1,10).
randint(1, 10)

# This is how you terminate a program:
import sys
from sys import *

print('hello')
# Uncomment the following section to use import sys example.
# sys.exit() # can be used too
# exit()
# This print function will never be called.
print('ok')

# Import pip modules. In this case import pyperclip.

import pyperclip

pyperclip.copy('Hello World')
pyperclip.paste()
