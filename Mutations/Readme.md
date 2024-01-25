
# 🚀 Immutable String Example in Python

## 🎉 Welcome

Welcome to an example showcasing the concept of working with immutable strings in Python! 🐍

## 📜 Code Example

### Given immutable string
We start with a string assigned to the variable `immutable_string`:

```python
immutable_string = "abracadabra"
```

### Accessing an Index
We can access individual characters in the string using index notation. For example, to get the character at index 5:

```python
index_5_element = immutable_string[5]
print(f"Element at index 5: {index_5_element}")
```

### Attempting Modification (Error)
Attempting to modify a character in an immutable string will result in a `TypeError`. Uncommenting the next line will raise the error:

```python
# immutable_string[0] = 'x'
```

### Demonstrating Immutability
We print the original string to highlight that the string remains unchanged after attempting modification:

```python
print(f"Original string: {immutable_string}")
```

## 🔍 Explanation

In this example, we illustrate the immutability of strings in Python. Once a string is created, you cannot modify its individual characters directly. This property is different from mutable data types like lists.

❌ Attempting to modify the string directly will result in a `TypeError` because strings are immutable in Python.

👉 The original string remains unchanged, emphasizing the immutability property.

## 🚀 Explore and Run

Feel free to explore and run the code to deepen your understanding! Happy coding! 🚀
```

