# Student Grades 📚🎓

## Problem Description 📝
You have the names and grades for each student in a class of N students. The task is to store this information in a nested list and identify the name(s) of any student(s) having the second lowest grade.

If there are multiple students with the second lowest grade, the names should be printed in alphabetical order, each name on a new line.

## Solution Approach 🤔💡
1. **Input Format:**
   - The input consists of an integer N (number of students).
   - For each student, input their name and grade separated by space.

2. **Output Format:**
   - Print the name(s) of the student(s) with the second lowest grade in alphabetical order.

3. **Algorithm:**
   - Store the student information (name and grade) in a nested list.
   - Find the second lowest grade among the students.
   - Collect the names of students having this second lowest grade.
   - Sort these names alphabetically.
   - Print each name on a new line.

4. **Example:**
   - Input:
     ```
     5
     Harry 37.21
     Berry 37.21
     Tina 37.2
     Akriti 41
     Harsh 39
     ```
   - Output:
     ```
     Berry
     Harry
     ```
   
5. **File Description:**
   - `student_grades.py`: Contains the Python code to solve the problem.
   - `example_input.txt`: Sample input for testing.
   - `example_output.txt`: Expected output corresponding to the sample input.

## How to Run ▶️🖥️
1. Clone the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the code is located.
4. Run the Python script using `python student_grades.py`.
5. Enter the number of students and their names with grades as prompted.
6. Check the output for the student(s) with the second lowest grade.

Feel free to modify the code or inputs to test different scenarios! 🛠️✨
