const sortedArr = require('../src/sortedArr.js');

describe('sortedArr Function', () => {
  test('should return 0 for an empty array', () => {
    expect(sortedArr([], 17)).toBe(0);
  });

  test('should return the correct index for an exact match', () => {
    expect(sortedArr([1, 3, 5, 7], 3)).toBe(1);
  });

  test('should return the correct index to insert a target in a sorted array', () => {
    expect(sortedArr([1, 3, 5, 7], 4)).toBe(2);
    expect(sortedArr([1, 3, 5, 7], 6)).toBe(3);
  });

  test('should return 0 when the target is smaller than the smallest element', () => {
    expect(sortedArr([1, 3, 5, 7], 0)).toBe(0);
  });

  test('should return the last index + 1 when the target is larger than the largest element', () => {
    expect(sortedArr([1, 3, 5, 7], 10)).toBe(4);
  });
});
