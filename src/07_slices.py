"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1
a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
s = slice(1,1)
print(s.start)

# Output the second-to-last element: 9
s = slice(-2)
print(a[s.stop])

# Output the last three elements in the array: [7, 9, 6]
s = slice(-3,6)
print(a[s])

# Output the two middle elements in the array: [1, 7]
s = slice(2,4)
print(a[s])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:5])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])