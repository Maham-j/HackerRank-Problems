# Person Class 

## Introduction

Welcome to the Person Class challenge! In this 🚀 challenge, you'll be diving into the world of Object-Oriented Programming (OOP) 🎭, specifically focusing on creating a `Person` class in a language that supports OOP.

## Task Overview

Your mission, should you choose to accept it 🕵️‍♂️, is to implement a `Person` class with certain requirements. The class should have an instance variable `age` and a constructor that sets the initial age, considering certain conditions. Additionally, the class should have methods to represent the passage of time and to determine the life stage of the person.

## Implementation Details

### Class: Person

#### Instance Variable

- **age**: An integer representing the age of the person.

#### Constructor

The class should have a constructor that takes an integer `initialAge` as a parameter. The constructor should:

1. Confirm that the argument passed as `initialAge` is not negative.
2. If `initialAge` is negative, set `age` to 0 and print "Age is not valid, setting age to 0." 🚫
3. If `initialAge` is non-negative, set `age` to the value of `initialAge`.

#### Methods

##### 1. `yearPasses()`

This method should increase the `age` instance variable by 1.

##### 2. `amIOld()`

This method should perform conditional actions based on the value of `age`:

- If `age` is less than 13, print "You are young." 👶
- If `age` is between 13 (inclusive) and 18 (exclusive), print "You are a teenager." 🧑‍🎓
- If `age` is 18 or older, print "You are old." 👴

## Example

```python
# Example usage of the Person class
person = Person(12)  # Creates a person with an initial age of 12

# Check the age and print the appropriate message
person.amIOld()  # Output: You are young. 👶

# Simulate the passage of a year
person.yearPasses()

# Check the age again after a year and print the appropriate message
person.amIOld()  # Output: You are a teenager. 🧑‍🎓
```

## Important Note

Do not remove or alter the stub code provided in the editor. The stub code is necessary for the main method to create instances of your `Person` class and test its functionality.

## License

This implementation is provided under the MIT License. Feel free to use, modify, and distribute this code as per the terms of the MIT License. See the LICENSE file for more details.


##  Contact: 

If you have any questions or suggestions about the script, feel free to reach out on GitHub or LinkedIn:

Discover more exciting coding projects on my [GitHub repository](https://github.com/Maham-j).

Connect with me on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267).

Connect with me on HackerRank: [HackerRank ](https://www.hackerrank.com/maham_jamil)


Happy coding! 🚀
