#!/bin/python3

import math
import os
import random
import re
import sys



# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s - List of chocolate squares on each day
#  2. INTEGER d - Desired sum of chocolate squares
#  3. INTEGER m - Number of consecutive days


def birthday(s, d, m):
    # Initialize a variable to keep track of the valid segment combinations
    total = 0
    
    # Iterate through the list of chocolate squares
    for i in range(len(s)):
        # Check if the sum of m consecutive days' chocolate squares equals d
        if sum(s[i:m+i]) == d:
            # If it matches, increment the total count
            total += 1
            
    # Return the total count of valid segment combinations
    return total

if __name__ == '__main__':
    # Open a file to write the output
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the total number of chocolate squares
    n = int(input().strip())

    # Read the list of chocolate squares for each day
    s = list(map(int, input().rstrip().split()))

    # Read the desired sum and number of consecutive days
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Call the birthday function and get the result
    result = birthday(s, d, m)

    print(result)

    # Write the result to the output file
    #fptr.write(str(result) + '\n')

    # Close the output file
    #fptr.close()
