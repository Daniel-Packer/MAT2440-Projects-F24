def linear_search(grades, target):
    """
    Searches for a specific grade in the list using Linear Search.
    Returns the index if found, otherwise returns -1.
    """
    for index, grade in enumerate(grades):
        if grade == target:
            return index
    return -1
