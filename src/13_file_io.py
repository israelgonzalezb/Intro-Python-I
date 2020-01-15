"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(THIS_FOLDER, "foo.txt")
file = open(file_path,"r")

print(file.read())
file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

file_path = os.path.join(THIS_FOLDER, "bar.txt")
file = open(file_path,"w")
file.write("hello\nworld\n!!!!!")
file = open(file_path,"r")

print(file.read())
file.close()