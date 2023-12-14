import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    
    num = 1
    for i in range(n):
        fac = num*(n-i)
        num = fac
    return num
        
    

if __name__ == '__main__':
    n = int(input().strip())

    result = extraLongFactorials(n)
    print(result)
