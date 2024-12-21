#include <iostream>
#include <vector>
using namespace std;

// Function to perform Linear Search
int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i; // return the index of the target
        }
    }
    return -1; // return -1 if the target is not found
}

// Function to find the maximum element in an array
int findMax(const vector<int>& arr) {
    int max = arr[0]; // Assume the first element is the max initially
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// Test function for linear search
void testLinearSearch() {
    vector<int> testData = {10, 20, 30, 40, 50};
    
    int result = linearSearch(testData, 30);
    if (result == 2) {
        cout << "Test 1 Passed: Element found at correct index" << endl;
    } else {
        cout << "Test 1 Failed" << endl;
    }

    result = linearSearch(testData, 60);
    if (result == -1) {
        cout << "Test 2 Passed: Element not found" << endl;
    } else {
        cout << "Test 2 Failed" << endl;
    }
}

// Test function for max search
void testFindMax() {
    vector<int> testData = {5, 10, 15, 20, 25};
    
    int result = findMax(testData);
    if (result == 25) {
        cout << "Test 1 Passed: Maximum value is correct" << endl;
    } else {
        cout << "Test 1 Failed" << endl;
    }
}

int main() {
    // Run all tests
    testLinearSearch();
    testFindMax();
    return 0;
}