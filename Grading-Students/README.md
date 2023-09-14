# 📚 **Grading Policy Rounding Tool** 📚

This Python script simulates a grading policy used at HackerLand University. The policy involves rounding student grades according to specific rules. Professor Sam has written this script to automate the grading process while adhering to the university's guidelines.

# 🔍 **Code Walkthrough:**

- **Grade Input:** The script starts by taking the total number of students, `n`, as input. It then prompts the user to enter the grades of individual students, which are stored in the `arr` list.

- **Rounding Logic:** The script proceeds to round the grades according to the specified rules. It first iterates through each student's grade in the `arr` list. If the grade is not already a failing grade (less than 38) and its remainder when divided by 5 is not zero, the script increments the grade until it becomes the next multiple of 5. The rounded grades are stored in the `rounded` list.

- **Final Adjustment:** The script then calculates the difference between the original grades and the rounded grades. If the difference is less than 3, the rounded grade is deemed acceptable and added to the `array` list. Otherwise, the original grade is retained.

- **Output and Result:** The script prints the original grades, the rounded grades, and the final array of grades that are either rounded up or left unchanged.

# 🔧 **Usage:**

1. Run the script in your Python environment.

2. Enter the number of students.

3. Enter the grades of individual students.

4. The script will calculate and display the rounded grades according to the rules.

# ⚙️ **Customization:**

Feel free to customize the script as needed:

- Modify the rounding logic if the university's policy changes.

- Add more conditions or adjustments to the grading policy.

# 🌐 **Find Me Online:**

Explore more of my coding projects on GitHub: GitHub: [https://github.com/Maham-j]

LinkedIn: [https://www.linkedin.com/in/maham-jamil-268584267]

Happy grading! 📝🎓👨‍🏫
