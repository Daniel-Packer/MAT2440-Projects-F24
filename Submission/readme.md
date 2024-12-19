# Project Overview

This project implements two fundamental algorithms: **Max Search** and **Linear Search**. These algorithms are widely used for searching tasks, also referred to as "find algorithms," which locate elements within a list or an array. Additionally, this project explores the use of Git and GitHub for version control and collaboration.

## Max Search Algorithm

The **Max Search Algorithm** identifies the largest number in a list of integers.

### Algorithm Description:

1. Assume the first element of the array as the maximum value.
2. Iterate through the array:
   - If the current value is greater than the assumed maximum, update the maximum value.
3. After completing the iteration, the `max` variable will contain the largest value in the array.
4. Return the `max` value.

### Python Implementation:

```python
def max_search(arr):
    # Assume the first element is the maximum
    max_val = arr[0]

    # Loop through the rest of the elements
    for num in arr[1:]:
        if num > max_val:
            max_val = num  # Update max_val if a larger element is found

    return max_val
```

### Test Example:

```python
def test_max_search():
    assert max_search([3, 1, 4, 1, 5, 9, 2, 6]) == 9
    assert max_search([10, 20, 30, 40]) == 40
    assert max_search([5, -1, 0, 2]) == 5
    print("All tests passed!")
```

---

## Linear Search Algorithm

The **Linear Search Algorithm** scans through a list in order to locate a target value.

### Algorithm Description:

1. Start at the first element of the array.
2. Compare each element with the target value:
   - If a match is found, return the current index.
   - Otherwise, proceed to the next element.
3. If the end of the list is reached without finding the target, return `-1`.

### Python Implementation:

```python
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return index of the found element
    return -1  # Return -1 if not found
```

### Test Example:

```python
def test_linear_search():
    assert linear_search([3, 1, 4, 1, 5, 9, 2, 6], 5) == 4
    assert linear_search([10, 20, 30, 40], 25) == -1
    assert linear_search([5, -1, 0, 2], -1) == 1
    print("All tests passed!")
```

---

## Conclusion

This project demonstrates the implementation of **Max Search** and **Linear Search** algorithms, which are foundational in computer science for searching operations. These basic algorithms form the groundwork for more complex searching techniques used in software engineering.

In addition to algorithm implementation, the project incorporates Git and GitHub for version control and collaboration. The use of these tools emphasizes teamwork and effective project management. Writing test cases and adhering to best practices in documentation have reinforced the importance of maintainability, reliability, and clarity in coding.

Through this project, we have highlighted the application of simple algorithms while embracing professional practices essential for successful software development.
