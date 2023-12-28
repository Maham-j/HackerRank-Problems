import math
import os 
import random
import re
import sys 

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beautifuldays = 0
    
    for i in range(i, j+1):
        num = str(i)
        reverse = str(i)[::-1]
        
        day = abs(int(num) - int(reverse))
        if day % k == 0:
            beautifuldays += 1
            
    return beautifuldays

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
