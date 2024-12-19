def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return index of the found element
    return -1  # Return -1 if not found
