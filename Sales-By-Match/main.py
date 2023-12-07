#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    counts = {}
    pairs = 0
    
    for element in ar:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    print(counts)
            
    for count in counts:
        pair = counts[count]//2
        pairs += pair
    return pairs
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
