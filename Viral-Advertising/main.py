import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    recipients = 5
    cumulative = 0
    
    for i in range(n):
        liked = recipients // 2
        shared = liked * 3
        cumulative += liked
        
#         print("recipients:",recipients)
        recipients = shared
#         print("liked:",liked)
        # print("cumulative:",cumulative)
    return cumulative
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
