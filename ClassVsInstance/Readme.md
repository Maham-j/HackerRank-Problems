# Person Class 


## 🚀 Introduction

Welcome to the Person Class challenge! 🎭 Dive into the exciting world of Object-Oriented Programming (OOP) with this task, where you'll create a `Person` class in a language that supports OOP.

## 🕵️‍♂️ Task Overview

Your mission: implement a `Person` class with an instance variable `age` and a constructor that sets the initial age, considering certain conditions. The class should also have methods to represent the passage of time and determine the life stage of the person.

## 🛠️ Implementation

### Class: Person

#### Instance Variable

- **age**: An integer representing the person's age.

#### Constructor

The constructor takes an integer `initialAge`:

1. If `initialAge` is negative, set `age` to 0 and print "Age is not valid, setting age to 0." 🚫
2. If non-negative, set `age` to the value of `initialAge`.

#### Methods

##### 1. `yearPasses()`

Increases the `age` instance variable by 1.

##### 2. `amIOld()`

Based on `age`:

- If less than 13, print "You are young." 👶
- If between 13 (inclusive) and 18 (exclusive), print "You are a teenager." 🧑‍🎓
- If 18 or older, print "You are old." 👴

## 🌟 Example

```python
# Example usage of the Person class
person = Person(12)  # Initial age: 12

# Check the age and print the appropriate message
person.amIOld()  # Output: You are young. 👶

# Simulate the passage of a year
person.yearPasses()

# Check the age again after a year and print the appropriate message
person.amIOld()  # Output: You are a teenager. 🧑‍🎓
```


## 📜 License

This implementation is provided under the MIT License. Feel free to use, modify, and distribute this code under the terms of the MIT License. See the LICENSE file for details.

Happy coding! 🚀

##  Contact: 

If you have any questions or suggestions about the script, feel free to reach out on GitHub or LinkedIn:

Discover more exciting coding projects on my [GitHub repository](https://github.com/Maham-j).

Connect with me on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267).

Connect with me on HackerRank: [HackerRank ](https://www.hackerrank.com/maham_jamil)

```
Happy coding! 🚀
