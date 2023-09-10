# Get input for the first and second names
name_1 = input('Enter first name:')
name_2 = input('Enter second name:')

# Combine the names and convert to lowercase
combined = (name_1 + name_2).lower()

# Count the occurrences of letters in "true" and "love"
true = combined.count('t') + combined.count('r') + combined.count('u') + combined.count('e')
love = combined.count('l') + combined.count('o') + combined.count('v') + combined.count('e')

# Calculate the love score by concatenating true and love counts
love_score = int(str(true) + str(love))
print(love_score)

# Determine the relationship status based on the love score
if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}% , you go together like coke and mentos')
elif (love_score < 50) or (love_score > 40):
    print(f'Your score is {love_score}% , you are alright together')
else:
    print(f'Your score is {love_score}%')
