## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print ("list dir", os.listdir("."))

# Let us check if this file is indeed a file!
print ("is file", os.path.isfile("./task_2.py"))
print ("is dir: False", os.path.isdir("./weekly_project"))
print ("is dir: True", os.path.isdir("./testdir"))


print("path", os.path.dirname(os.path.abspath(".")))

# Does the file end with .py?
print ("ends with", "./ex.py".endswith(".py"))