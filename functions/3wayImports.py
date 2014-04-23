# Generic Imports
# must type "math."
import math
print math.sqrt(225)
everything = dir(math) # Sets everything to a list of things from math
print everything

# Function Imports
# not neccessary to type "math."
from math import sqrt
print sqrt(225)

# Universal Imports (Not recommended)
# not neccessary to type "math."
from math import *
print sqrt(225)
