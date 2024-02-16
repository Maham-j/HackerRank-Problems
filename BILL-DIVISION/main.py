#!/bin/python3
  
import math     
import os    
import random  
import re 
import sys  
 
# The function to calculate the refund or print "Bon Appetit"
def bonAppetit(bill, k, b):
    total_bill = 0
    
    # Remove the item Anna didn't eat from the bill
    bill.remove(bill[k])
    
    # Calculate the total bill amount after excluding the item
    for i in bill:
        total_bill += i
    
    # Calculate the bill division amount for each person
    bill_division = total_bill // 2
    
    # Check if the calculated division matches Anna's contribution
    if bill_division == b:
        print('Bon Appetit')  # Print "Bon Appetit" if the contribution is correct
    else:
        refund = abs(bill_division - b)  # Calculate the refund amount if contribution is incorrect
        print(refund)  # Print the refund amount

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())

    bonAppetit(bill, k, b)  # Call the bonAppetit function with the provided inputs
