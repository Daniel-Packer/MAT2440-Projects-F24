from src.linear_search import linear_search

def test_linear_search():
    # Test case 1: Element found in the list
    grades = [60, 70, 80, 90]
    assert linear_search(grades, 80) == 2
    
    # Test case 2: Element not found
    assert linear_search(grades, 100) == -1
    
    # Test case 3: Duplicate elements
    grades = [60, 70, 70, 90]
    assert linear_search(grades, 70) == 1

test_linear_search()
print("Linear Search Tests Passed.")
