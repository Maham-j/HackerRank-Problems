# 🤖 Divisible Sum Pairs Finder 

A Python function to find pairs of integers in an array that meet a specific divisibility criterion.

## 💡 Problem Statement

Given an array of integers `ar` and a positive integer `k`, we want to determine the number of pairs `(i, j)` where `i < j` and `ar[i] + ar[j]` is divisible by `k`.

### Example

```python
ar = [1, 2, 3, 4, 5, 6]
k = 5

Result: 3

# The pairs [1, 4], [2, 3], and [4, 6] meet the criteria since their sums are divisible by 5.
```

## 🚀 Function Usage

You can use the `divisibleSumPairs` function to find the number of such pairs in an array. Here's how to use it:

```python
from divisible_sum_pairs import divisibleSumPairs

ar = [1, 2, 3, 4, 5, 6]
k = 5

result = divisibleSumPairs(len(ar), k, ar)
print(f"Number of divisible sum pairs: {result}")
```

## 🔧 Implementation

The `divisibleSumPairs` function takes three parameters:

1. `n` - The number of elements in the array.
2. `k` - The positive integer divisor.
3. `ar` - The array of integers.

It uses nested loops to iterate through all pairs of elements in the array and checks whether their sum is divisible by `k`. The function returns the count of such pairs.

## 🌟 Contribution

Contributions are welcome! If you have any improvements, bug fixes, or feature enhancements, please fork this repository, make your changes, and submit a pull request.

Discover more exciting coding projects on my [GitHub repository](https://github.com/Maham-j).

Connect with me on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267).

Connect with me on HackerRank: [HackerRank ](https://www.hackerrank.com/maham_jamil)


## 📄 License

This project is open-source and available under the GNU General Public License v3.0.. See the [GNU General Public License v3.0..](LICENSE) file for details.

---

Made with ❤️ by [MAHAM.J](https://github.com/Maham-j)

If you find this function helpful, show your support by giving it a ⭐️!
