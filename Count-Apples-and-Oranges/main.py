#!/bin/python3

import math
import os 
import random
import re
import sys
 
# The function to count apples and oranges that land within a house's range
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_land = 0  # Counter for apples that land within the range
    oranges_land = 0  # Counter for oranges that land within the range
    
    # Iterate through each distance where apples fell
    for i in apples:
        total_apples = i + a  # Calculate the absolute position of the apple
        if total_apples >= s and total_apples <= t:
            apples_land += 1  # If apple's position is within the house's range, increment counter
    
    print(apples_land)  # Print the count of apples that landed within the house's range
    
    # Iterate through each distance where oranges fell
    for j in oranges:
        total_oranges = j + b  # Calculate the absolute position of the orange
        if total_oranges >= s and total_oranges <= t:
            oranges_land += 1  # If orange's position is within the house's range, increment counter
            
    print(oranges_land)  # Print the count of oranges that landed within the house's range

if __name__ == '__main__':
    # Read the first line of input: house range (s, t)
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])  # Starting point of the house
    t = int(first_multiple_input[1])  # Ending point of the house
    
    # Read the second line of input: tree locations (a, b)
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])  # Position of the apple tree
    b = int(second_multiple_input[1])  # Position of the orange tree
    
    # Read the third line of input: number of apples and oranges (m, n)
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])  # Number of apples
    n = int(third_multiple_input[1])  # Number of oranges
    
    # Read the fourth line of input: distances where apples fell
    apples = list(map(int, input().rstrip().split()))
    
    # Read the fifth line of input: distances where oranges fell
    oranges = list(map(int, input().rstrip().split()))
