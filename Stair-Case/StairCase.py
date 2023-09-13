# Importing necessary modules
import math
import os
import random
import re
import sys

# Defining 'staircase' function with input 'n'
def staircase(n):
    # Loop through rows
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(' ', end='')
        
        # Print '#' characters
        for k in range(i + 1):
            print('#', end='')
        
        # Move to the next line
        print()

# Main program
if __name__ == '__main__':
    # Read integer 'n' from input
    n = int(input().strip())
    
    # Call 'staircase' function
    staircase(n)
