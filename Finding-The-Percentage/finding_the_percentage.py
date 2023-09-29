if __name__ == '__main__':
    # Read the number of students (n) from input.
    n = int(input())
    # Create an empty dictionary to store student names and their scores.
    student_marks = {}
    
    # Loop to read student names and scores.
    for _ in range(n):
        # Read the input line containing the name and scores as a list of strings.
        name, *line = input().split()
        # Convert the list of score strings to a list of floating-point numbers.
        scores = list(map(float, line))
        # Store the student's scores in the dictionary using their name as the key.
        student_marks[name] = scores

    # Read the query name (the name of the student for whom we want to calculate the average score).
    query_name = input()
    
    # Initialize a variable to calculate the total score.
    total_score = 0
    
    # Check if the query_name exists in the student_marks dictionary.
    if query_name in student_marks:
        # Loop through the scores of the student with the query_name.
        for score in student_marks[query_name]:
            total_score += score
        # Calculate the average score and format it with two decimal places.
        formatted = '{:.2f}'.format(total_score / len(student_marks[query_name]))
        # Print the formatted average score for the student.
        print(formatted)
