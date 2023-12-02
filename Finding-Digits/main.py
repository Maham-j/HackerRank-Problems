import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    divisible = 0
    
    new_n = str(n)
    for num in new_n:
        if num == '0':
            continue
        elif n % (int(num)) == 0:
            divisible += 1
            
    return divisible
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
    print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
