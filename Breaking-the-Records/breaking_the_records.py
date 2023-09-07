#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as a parameter.
#

def breakingRecords(scores):
    # Initialize variables to track maximum and minimum scores and their corresponding records.
    maximum = -float('inf')
    minimum = float('inf')
    
    min_records = 0
    max_records = 0

    # Loop through the 'scores' list to calculate maximum and minimum records.
    for score in scores:
        # Check if the current score is greater than the current maximum score.
        if score > maximum:
            maximum = score
            max_records += 1

        # Check if the current score is less than the current minimum score.
        if score < minimum:
            minimum = score
            min_records += 1

    # Return a list containing the maximum and minimum records.
    return [max_records-1, min_records-1]

if __name__ == '__main__':
    # Open a file to write the output.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of scores.
    n = int(input().strip())

    # Read the list of scores as integers.
    scores = list(map(int, input().rstrip().split()))

    # Call the breakingRecords function to calculate records.
    result = breakingRecords(scores)

    # Write the results as space-separated integers to the output file.
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    # Close the output file.
    fptr.close()
