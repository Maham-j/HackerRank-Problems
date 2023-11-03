# Define the function for counting tallest candles on a birthday cake 
def birthdayCakeCandles():
    # Read the number of candles
    n = int(input())
    # Initialize an empty list to store candle heights 
    arr = []  
    # Initialize variables to track tallest candle and count of tallest candles
    tallest_candle = 0
    count = 0
    
    # Loop to input candle heights
    for i in range(n):
        # Read the height of the current candle
        height = int(input())
        # Append the height to the list
        arr.append(height)
    
    # Loop to find the tallest candle
    for height in arr:
        # Update tallest_candle if a taller candle is found
        if height > tallest_candle:
            tallest_candle = height
    
    # Loop to count the number of tallest candles
    for i in arr:
        # Increment count if the current candle's height matches the tallest
        if i == tallest_candle:
            count += 1
    
    # Return the count of tallest candles
    return count

# Call the function to get the result
birthdayCakeCandles()
