
## 🧦 Sock Pairing Counter 🧦

This program takes an array of integers representing the color of each sock and determines the number of pairs with matching colors.

### Usage 🚀

1. **Input:** Provide an array of integers representing sock colors.
2. **Output:** Receive the count of pairs of socks with matching colors.

### Example 💡

```python
# Sample Input
socks = [1, 2, 1, 2, 1, 3, 2]

# Output
pairs = count_sock_pairs(socks)
print(f"Number of pairs: {pairs}")
```

### Function Explanation ℹ️

`count_sock_pairs(socks: List[int]) -> int`: This function takes a list of integers representing sock colors and returns the count of pairs.

### Implementation Details 🛠️

- The program iterates through the array of sock colors and uses a dictionary to keep track of the count of each color.
- For each color, it calculates the number of pairs by dividing the count by 2 (as each pair consists of two socks of the same color) and adds this count to the total pairs.

### Running the Code ▶️

1. Clone the repository.
2. Run the Python file with your desired input.
   ```
   python sock_pair_counter.py
   ```

## Connect with Me 🌐 

Discover more exciting coding projects on my [GitHub repository](https://github.com/Maham-j)

Connect with me on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267)

Connect with me on HackerRank: [HackerRank ](https://www.hackerrank.com/maham_jamil)

---

Happy coding! 🚀
