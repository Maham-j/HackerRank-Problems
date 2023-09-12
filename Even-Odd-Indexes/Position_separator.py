# Get the number of test cases from the user
n = int(input())

# Loop through each test case
for _ in range(n):
    # Get the input string for the current test case
    total = input()
    
    # Initialize empty strings for even and odd positions
    even = ''
    odd = ''
    
    # Loop through each character in the input string
    for i in range(len(total)):
        # Check if the index 'i' is even
        if i % 2 == 0:
            even += total[i]  # Add the character to the even string
        else:
            odd += total[i]  # Add the character to the odd string
            
    # Print the concatenated even and odd strings separated by a space
    print(even + ' ' + odd)
