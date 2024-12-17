# Implement the linear search algorithm using PYTHON
# Let's first create an array with numbers in them

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Create a linear search function

def the_linear_search(arr, integer):
    
    for i in range(len(arr)):
        if (arr[i] == integer):
            return i   # Function will send back i if it matches what the target (integer) is
    # if arr[i] doesn't equal 'integer' the function will return -1
    return -1
    
    
# Now let's set a target integer and call the function
integer = 11
test = the_linear_search(numbers, integer)

if test != -1:
    print(test)
    
    
