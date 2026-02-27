import numpy as np

"""
Student Marks Analyzer using NumPy

Features:
- Student totals
- Student averages
- Subject averages
- Topper detection
- High scorer filtering
- Class statistics
"""

# Rows = student = 4 , Column = subject = 4

marks = np.array([[98,78,99,67],
                  [67,89,76,65,],
                  [45,67,86,59],
                  [67,77,87,76]])

# axis = 0 (Operations for Row)
# axis = 1 (Operations for column)

# Total marks of each student
total_marks_1 = np.sum(marks[0], axis=0)
total_marks_2 = np.sum(marks[1], axis=0)
total_marks_3 = np.sum(marks[2], axis=0)
total_marks_4 = np.sum(marks[3], axis=0)

# Average marks of each subject
subject_avg = np.mean(marks, axis=0)

# Average marks of each student
student_avg = np.mean(marks, axis=1)

# Topper student index
topper = np.argmax(student_avg)

# Students who scored more than 85 in all subjects
high_scorers = marks[np.all(marks > 85, axis=1)]

print("Total marks of student 1: ", total_marks_1)
print("Total marks of student 2: ", total_marks_2)
print("Total marks of student 3: ", total_marks_3)
print("Total marks of student 4: ", total_marks_4)

print("Student Average:", student_avg)
print("Subject Average:", subject_avg)
print("Topper Student Index:", topper)
print("High Scorers:\n", high_scorers)

