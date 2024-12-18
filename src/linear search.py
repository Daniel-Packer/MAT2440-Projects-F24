# Implement the linear search algorithm using PYTHON

# Create a linear search function

def the_linear_search(arr, integer):
    
    for i in range(len(arr)):
        if (arr[i] == integer):
            return i   # Function will send back i if it matches what the target (integer) is
    # if arr[i] doesn't equal 'integer' the function will return -1
    return -1
