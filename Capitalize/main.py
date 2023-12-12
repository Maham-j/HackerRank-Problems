
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    capitalize = []
    
    for word in words:
        modified = word.capitalize()
        capitalize.append(modified)
        
    return ' '.join(capitalize)

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
