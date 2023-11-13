# Phone Book 

## 📱 Introduction

Welcome to the Phone Book challenge! 📞 In this task, you will be building a phone book using a Dictionary/Map/HashMap data structure to map friends' names to their respective phone numbers.

## 📚 Task Overview

Your goal is to assemble a phone book that efficiently associates names with their corresponding phone numbers. You will then receive an unknown number of names to query your phone book for. For each queried name, print the associated entry from your phone book in the form `name=phoneNumber`. If an entry for the name is not found, print `name Not found` instead.

## 🛠️ Implementation

### Data Structure: Phone Book (Dictionary/Map/HashMap)

#### Key-Value Pair

- **Key**: Friend's name
- **Value**: Corresponding phone number

### Methods

#### 1. `addContact(name, phoneNumber)`

This method adds a new contact to the phone book.

#### 2. `queryContact(name)`

This method queries the phone book for a given name:

- If the name is found, print `name=phoneNumber`.
- If the name is not found, print `name Not found`.

## 🌟 Example

```python
# Example usage of the Phone Book
phoneBook = PhoneBook()

# Add contacts to the phone book
phoneBook.addContact("Alice", "1234567890")
phoneBook.addContact("Bob", "9876543210")

# Query the phone book for names
phoneBook.queryContact("Alice")  # Output: Alice=1234567890
phoneBook.queryContact("Charlie")  # Output: Charlie Not found
```

## 🚨 Important Note

You should implement the `PhoneBook` class with the specified methods and utilize it to efficiently manage contacts.

## 📜 License

This implementation is provided under the MIT License. Feel free to use, modify, and distribute this code under the terms of the MIT License. See the LICENSE file for details.

## 📞 Contact: 

If you have any questions or suggestions about the script, feel free to reach out on GitHub or LinkedIn:

Discover more exciting coding projects on my [GitHub repository](https://github.com/Maham-j).

Connect with me on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267).

Connect with me on HackerRank: [HackerRank ](https://www.hackerrank.com/maham_jamil)


Happy coding! 📱
