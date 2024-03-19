import math 
import os     
import random
import re
import sys    
 

  

# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
 

def aVeryBigSum(ar):
    # Initialize a variable to store the sum
    sum = 0
    
    # Loop through each element in the input list 'ar'
    for i in ar:
        # Add the current element 'i' to the sum
        sum += i
        
    # Return the final sum after iterating through all elements
    return sum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
 
