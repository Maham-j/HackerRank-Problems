# Class Cancellation 

## 🕒 Introduction

Welcome to the Class Cancellation challenge! 🎓 In this problem, you're presented with a scenario where a Discrete Mathematics professor plans to cancel the class based on the arrival times of the students. The professor will cancel the class if fewer than a certain number of students arrive on time.

## 📝 Problem Description

The professor will cancel the class if the number of students arriving on time is below a specified threshold. Arrival times range from on time (arrivalTime <= 0) to arriving late (arrivalTime > 0).

### Function Description

Your task is to create a function that determines if the class should be canceled based on the given criteria.

#### Function Signature

```python
def is_class_canceled(threshold, arrival_times):
    pass
```

#### Parameters

- **threshold**: An integer representing the minimum number of students required for the class not to be canceled.
- **arrival_times**: A list or array of integers representing the arrival times of the students.

#### Returns

- **bool**: Return `True` if the class should be canceled; otherwise, return `False`.

## 🧠 Implementation Details

You need to implement the `is_class_canceled` function that takes in the threshold and a list of arrival times. The function should evaluate if the number of students arriving on time is less than the specified threshold.

## 🌟 Example

```python
# Example usage of the is_class_canceled function
threshold = 3
arrival_times = [0, -1, 2, 1]

result = is_class_canceled(threshold, arrival_times)  # Evaluates if class should be canceled

print(result)  # Output: False
```

## 🚨 Important Note

Ensure that your function properly evaluates whether the class should be canceled or not based on the given threshold and arrival times.

## 📜 License

This implementation is provided under the MIT License. You are free to use, modify, and distribute this code as per the terms of the MIT License. See the LICENSE file for more details.

## Connect with Me 🌐 

Discover more exciting coding projects on my [GitHub repository](https://github.com/Maham-j)

Connect with me on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267)

Connect with me on HackerRank: [HackerRank ](https://www.hackerrank.com/maham_jamil)

---

Happy coding! 🕒🎓
