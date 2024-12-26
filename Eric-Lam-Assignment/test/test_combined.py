from src.bubble_sort import bubble_sort
from src.linear_search import linear_search

def test_combined():
    grades = [88, 72, 95, 60, 85]
    sorted_grades = bubble_sort(grades)
    assert sorted_grades == [60, 72, 85, 88, 95]
    
    # Test searching for an element
    assert linear_search(sorted_grades, 85) == 2
    assert linear_search(sorted_grades, 100) == -1

test_combined()
print("Combined Tests Passed.")
