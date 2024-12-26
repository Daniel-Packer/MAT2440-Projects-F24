def bubble_sort(grades):
    """
    Sorts the list of grades in ascending order using Bubble Sort.
    """
    n = len(grades)
    for i in range(n):
        for j in range(0, n-i-1):
            if grades[j] > grades[j+1]:
                grades[j], grades[j+1] = grades[j+1], grades[j]
    return grades
