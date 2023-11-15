import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    fac = 1
    # Write your code here
    for i in range(n):
        fac *= (n-i)
    return fac

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
