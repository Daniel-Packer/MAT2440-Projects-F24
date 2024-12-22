def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1  # Base case: not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)

if __name__ == "__main__":
    example = [1, 3, 5, 7, 9, 11]
    target = 7
    result = recursive_binary_search(example, target, 0, len(example) - 1)
    print(f"Target {target} found at index: {result}")
