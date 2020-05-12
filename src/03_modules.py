"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for line in sys.argv:
    print("line arguments in sys.argv: ", line)

# Print out the OS platform you're using:
print("OS platform: ", sys.platform)

# Print out the version of Python you're using:
print("Version of Python: ", sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("PID current process: ", os.getpid())

# Print the current working directory (cwd):
print("current working directory: ", os.getcwd())

# Print out your machine's login name
print("machine login name: ", os.getlogin())
