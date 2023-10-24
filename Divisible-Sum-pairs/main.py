#!/bin/python3 

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n - The length of the input array 'ar'.
#  2. INTEGER k - The divisor.
#  3. INTEGER_ARRAY ar - An array of integers.

def divisibleSumPairs(n, k, ar):
    # Initialize a variable 'total' to keep track of the count of pairs that meet the condition.
    total = 0

    # Loop through the array with two nested loops.
    for i in range(n-1):
        for j in range(i+1, n):
            # Check if the sum of elements at indices 'i' and 'j' is divisible by 'k'.
            if (ar[i] + ar[j]) % k == 0:
                # If it is divisible, increment the 'total' count.
                total += 1

    # Return the total count of pairs that satisfy the condition.
    return total

if __name__ == '__main__':
    # Read input values from the standard input.
    first_multiple_input = input().rstrip().split()

    # Parse the input values to integers.
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    # Read the array of integers from the standard input.
    ar = list(map(int, input().rstrip().split()))

    # Call the 'divisibleSumPairs' function with the provided input values.
    result = divisibleSumPairs(n, k, ar)

    # Write the result to the standard output.
    fptr.write(str(result) + '\n')

    # Close the output file.
    fptr.close()
