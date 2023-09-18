import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())  # Read the size of the array
    array = list(map(int, input().strip().split()))  # Read the array elements

    reversed_array = array[::-1]  # Reverse the array using slicing
    # Print the reversed array elements as a space-separated list
    for num in reversed_array:
        print(num, end=' ')
