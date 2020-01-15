# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if x == 0:
        print(f'{x} is 0')
    elif x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

is_even(num)
