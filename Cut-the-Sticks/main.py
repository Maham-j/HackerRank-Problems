#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    
    results = []
    while len(arr) > 0:
        results.append(len(arr))
        
        # Find the minimum stick length in the current array
        min_length = min(arr)
        
        # Cut each stick in the array by the minimum length
        arr = [x - min_length for x in arr]
        
        # Remove all zero-length sticks
        arr = [x for x in arr if x > 0]
        
        # Print the number of sticks remaining after this round of cuts
        
    
    return results 

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print(result)
