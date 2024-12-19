def max_search(arr):
    # Assume the first element is the maximum
    max_val = arr[0]
    
    # Loop through the rest of the elements
    for num in arr[1:]:
        if num > max_val:
            max_val = num  # Update max_val if a larger element is found
    
    return max_val
