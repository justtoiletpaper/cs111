# import the whole module
import link
L = link.Linkclass(2)

# import a specific class or function to your global frame
from link import Linkclass
L = linkclass(2)    # No longer need to specify import file ######.linkclass

# import all classes or functions into your global frame
from link import *

# Importing with an alias
# A class or functino: (not recommended)
from link import Linkclass as LL
L = LL(2)
# A module as a whole (very common - is acceptable):
import link as ll
L = ll.linkclass(2)

# This command runs a module:
python module.py
# When run like that, Python sets a global variable __name__ to "__main__". Thaat means you often see code at the
# bottom of modules like this:
if __name__ == "__main__":
    # Use the code in this module somehow

"""A Python Package is a way of bundling multiple modules together.
the Python Package Index is a repository of packages for Python:"""
# Install packages using pip
pip(3) install byuimage
# You may also need to use the longhand form if your system is grabbing pip from a different
# installation than the actual python interpreter:
python(3) -m pip install byuimage