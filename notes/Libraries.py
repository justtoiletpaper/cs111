# Libraries are just code that is external to your program that you want to use
# == Someone else's code, reusing your own code, code your writing now but doesn't usably fit in one file

# import the entire library
import operator

# To use functions and objects that are imported like this, we reference them using library_name.function_name
# Libraries can be bound to a different name if desired
sum = operator_add(3, 7)

# If you dont want to have to use the library name each time, you can import this way:
from operator import *
sum = add(3, 7)
# * Only recommended for small libraries where you already know all the names

# Only import what you want from the library:
import operator add, sub, mul

# When you want to install new libraries, you use the pip common in a terminal window
pip install byuimage
# sometimes this doesn't work, and you need to uses the longer form:
python -m pip install byuimage
# This installs the library and then you can import it in your Python code





