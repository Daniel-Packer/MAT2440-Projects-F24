import math

# This file does not run any code since my intnetion with it is to import it for other parts of this project.
# This file holds all the searching alogrithms I implemented ( linear, binary, and jump search ).

def linear_search(an_array, target, start=None, end=None):
    """
    Linear search: Finds the target value in an array.
    Returns the index of the target if found, else None.
    """
    
    # This chunk of code is to make sure even if a defualt isnt provided for start or end it assigns a value to them.
    if start == None or start < 0:
        start = 0
    if end == None or end > len(an_array):
        end = len(an_array)
        
        
    for i in range(start, end):
        if an_array[i] == target:
            return i
    # If target is not found return none
    return None

def binary_search(an_array, target, start=None, end=None):
    """
    Binary search: Efficiently finds the target value in a SORTED array.
    Returns the index of the target if found, else None.
    """
    # This ensures that no matter what the code is started at the max range of the array.
    if start is None:
        start = 0
    if end is None:
        end = len(an_array) - 1

    # This ensures if the range is invalide, the target is not in the array.
    if start > end:
        return None
    
    
    else:
        mid = (start + end) // 2
        
        if an_array[mid] == target:
            return mid
        elif an_array[mid] < target:
            start = mid + 1
            return binary_search(an_array, target, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, start, end)

def jump_search(an_array, target):
    """
    Jump search: Searches a sorted array using fixed block sizes.
    Returns the index of the target if found, else None.
    """
    # Calculate block size using square root of the array length and floor divison to get an integer 
    block = int(math.sqrt(len(an_array))//1)   
    
    start = 0
    end = block - 1
    while (end < len(an_array)):
        if target == an_array[end]:
            return end
        if target < an_array[end]:
            return linear_search(an_array, target, start , end)
        if target > an_array[end]:
            start = start + block 
            end = end + block

    # If target isnt found in any block, does linear search on all the remaining elements in the hopes of finding it
    return linear_search(an_array, target, start, len(an_array))
