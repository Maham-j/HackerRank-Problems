
## ⌨️ Most Expensive Keyboard and USB Drive Finder 🔌

This program helps determine the most expensive computer keyboard and USB drive that can be purchased within a given budget.

### Usage 🚀

1. **Input:** Provide price lists for keyboards and USB drives, along with a budget.
2. **Output:** Receive the total cost of the most expensive keyboard and USB drive combination that fits within the budget. If it's not possible to buy both items, return -1.

### Example 💡

```python
# Sample Input
keyboards = [40, 35, 70, 15]
drives = [20, 15, 25, 10]
budget = 50

# Output
total_cost = expensive_keyboard_and_drive(keyboards, drives, budget)
print(f"Total cost of most expensive pair: ${total_cost}")
```

### Function Explanation ℹ️

`expensive_keyboard_and_drive(keyboards: List[int], drives: List[int], budget: int) -> int`: This function takes two lists of integers representing the prices of keyboards and USB drives, along with a budget. It returns the total cost of the most expensive combination that fits within the budget. If it's not possible to buy both items, it returns -1.

### Implementation Details 🛠️

- The program iterates through all possible combinations of a keyboard and a USB drive within the budget.
- It finds the combination with the maximum cost that doesn't exceed the budget.
- If such a combination is found, it returns the total cost. Otherwise, it returns -1.

### Running the Code ▶️

1. Clone the repository.
2. Run the Python file with your desired input.
   ```
   python expensive_keyboard_and_drive.py
   ```

### Author ✍️

[Your Name]

---

Feel free to adapt and expand upon this README according to your specific project or use case.
