#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    length = len(word)
    
    alphabets = []
    indexes = []
    for i in range(97,123):
        alphabets.append(chr(i))

    for i in word:
        indexes.append(alphabets.index(i))
    
    highlight = []
    for j in indexes:
        highlight.append(h[j])
        
    return length * max(highlight)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
