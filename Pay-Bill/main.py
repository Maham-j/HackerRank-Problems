import random

# List of names
name = input('Input names separated by comma: ')
names = name.split(',')

# Randomly select a name from the list
selected_name = random.choice(names)

# Print the selected name with capitalization
print(f'{selected_name.capitalize()} is going to buy the meal today!')
