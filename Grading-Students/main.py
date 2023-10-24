def gradingStudents():
    # Input the number of students 
    n = int(input())
    arr = []  # Initialize an array to store original marks
    array = []  # Initialize an array to store final grades
    
    # Input marks for each student and store in the array
    for i in range(n):
        marks = int(input())
        arr.append(marks)
    print(arr)
    
    rounded = []  # Initialize an array to store rounded marks
    
    # Round marks to the nearest multiple of 5 if above 38
    for i in arr:
        while i % 5 != 0 and i >= 38:
            i += 1
        rounded.append(i)
    print(rounded)
    
    # Determine final grades based on rounding rules
    for i in range(len(arr)):
        result = rounded[i] - arr[i]
        if result < 3:
            array.append(rounded[i])  # Append rounded mark if difference < 3
        else:
            array.append(arr[i])  # Keep original mark if difference >= 3
    
    print(array)

# Call the gradingStudents function to execute the code
gradingStudents()
