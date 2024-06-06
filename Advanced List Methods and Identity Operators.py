# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_and_attended = submitted[0], submitted[2]
print(submitted_and_attended)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

if submitted and attended:
    print("same")
else:
    print("not the same")

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended.remove("Eve")
attended.remove("Frank")
print(attended)


