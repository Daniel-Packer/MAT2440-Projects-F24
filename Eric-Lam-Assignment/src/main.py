from bubble_sort import bubble_sort
from linear_search import linear_search
import random

# Generate a list of random student grades
grades = [random.randint(50, 100) for _ in range(20)]
print("Original Grades:", grades)

# Sort the grades
sorted_grades = bubble_sort(grades)
print("Sorted Grades:", sorted_grades)

# Ask user to search for a grade
try:
    target_grade = int(input("\nEnter a grade to search: "))
    result = linear_search(sorted_grades, target_grade)
    if result != -1:
        print(f"Grade {target_grade} found at index {result} in the sorted list.")
    else:
        print(f"Grade {target_grade} not found in the list.")
except ValueError:
    print("Invalid input! Please enter a valid grade (integer).")
