def test_bubble_sort():
    # Test case 1: Random unsorted list
    grades = [90, 85, 70, 65, 80]
    assert bubble_sort(grades) == [65, 70, 80, 85, 90]
    
    # Test case 2: Already sorted list
    grades = [50, 60, 70, 80]
    assert bubble_sort(grades) == [50, 60, 70, 80]
    
    # Test case 3: Duplicate values
    grades = [70, 70, 90, 60]
    assert bubble_sort(grades) == [60, 70, 70, 90]

test_bubble_sort()
print("Bubble Sort Tests Passed.")
