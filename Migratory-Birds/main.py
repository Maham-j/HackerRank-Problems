#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def migratoryBirds(arr):
    # Initialize a list to count the occurrences of each bird type (types 1 to 5).
    bird_counts = [0] * 6  # There are 5 types of birds (1 to 5)

    # Loop through the given list of bird sightings and count each type.
    for bird in arr:
        bird_counts[bird] += 1
    
    # Find the maximum count of bird sightings.
    maximum_count = max(bird_counts)
    
    # Find the index (bird type) with the maximum count, which represents the most migratory bird.
    most_migratory_bird = bird_counts.index(maximum_count)
    
    # Return the type of the most migratory bird.
    return most_migratory_bird

if __name__ == '__main__':
    # Read the total count of bird sightings.
    arr_count = int(input().strip())

    # Read the list of bird sightings as integers.
    arr = list(map(int, input().rstrip().split()))

    # Call the migratoryBirds function to find the most migratory bird type.
    result = migratoryBirds(arr)

    # Print the result (most migratory bird type) directly to the console.
    print(result)
