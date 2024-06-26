# To open a file:
# myFile = open(,filename, <access mode>)
from BasicPythonSyntax import myFile

# To close a file:
# MyFile.close()
# Otherwise, the file closes when the script ends.

# The 'with' command:
# with open(<filename>, <access mode>) as <name>:
    # Code that uses the file name
# The file will automatically close at the end of the indented code

data = myFile.read()    # The file is converted into a single string object

data_lines = myFile.readlines()     # The file reads all the file as a list of strings

oneline = myFile.readline()     # The file reads a single line

myFile.write(line)

myFile.writelines()




