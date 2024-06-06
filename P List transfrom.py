# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)

print(grades)

# Task 2: Calculate the average grade and display it.

average_grades = sum(grades) / len(grades)
print(average_grades)

# Task 3: Replace any grade below 80 with the value 

grades[7] = "failed"
grades[8] = "failed"
grades[9] = "failed"
print(grades)