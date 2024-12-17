# README

## Project Description

This project implements the `sortedArr` function, which determines the appropriate index for a target value in a sorted array. The function can:

- Return the index if the target value exists in the array.
- Return the index where the target should be inserted if it does not exist.
- Handle edge cases like an empty array, targets smaller than the smallest element, or larger than the largest element.

### What Was Done

- **Core Algorithm**: Implemented the `sortedArr` function to meet the requirements described above.
- **Test Cases**: Created a set of test cases to ensure the function behaves as expected for different inputs and edge cases.
- **File Organization**: Structured the project into distinct files for the implementation and the tests.

### Algorithm Used

The algorithm used in the `sortedArr` function is a linear search. It iterates through the sorted array to find the target value or determine the appropriate insertion index. The steps are as follows:

1. Traverse the array step-by-step.
2. Check if the target value matches the current element or falls between the current element and the next element.
3. Handle edge cases such as:
   - If the array is empty, return 0.
   - If the target is smaller than the first element, return 0.
   - If the target is larger than the last element, return the index for insertion at the end.

### Worst-Case Scenario

The worst-case time complexity of this algorithm is **O(n)**, where `n` is the size of the array. This occurs when:

- The target value is larger than all elements in the array, requiring traversal through the entire array.
- The array is empty or contains only one element (though the time complexity remains O(1) for these cases due to their simplicity).

While the algorithm is simple and effective for smaller datasets, it is not the most efficient for larger datasets compared to binary search, which has a time complexity of **O(log n)** for sorted arrays.


## How to Run the Files

### Prerequisites

- Install [Node.js](https://nodejs.org/).

### Steps to Run

For additional guidance on unit testing, I refer to this [YouTube video](https://www.youtube.com/watch?v=diC9TvwXSUM).

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the test cases:
   ```bash
   node test/sortedArr.test.js
   ```
   or 
   ```bash
   npm test
   ```
   This will execute the test cases and display the results in the terminal.

### Expected Output

When you run the tests, you should see output similar to:

```
Running Tests for sortedArr...
✅ should return 0 for an empty array
✅ should return the correct index for an exact match
✅ should return the correct index to insert a target in a sorted array
✅ should return 0 when the target is smaller than the smallest element
✅ should return the last index + 1 when the target is larger than the largest element
```

## Organization of Submission

The project is organized as follows:

```
Staceyann_king_submission/
├── src/
│   └── sortedArr.js   #Contains the implementation of the `sortedArr` function
├── test/
│   └── sortedArr.test.js  # Contains test cases for validating the function
├── README.md              # Project documentation (this file)
```

- **index.js**: Implements the `sortedArr` function.
- **test/sortedArr.test.js**: Contains test cases to verify the correctness of the function.
- **README.md**: Describes the project, how to run it, and its organization.

---

Thank you for reviewing this submission! If you have any questions or need further assistance, feel free to reach out.

