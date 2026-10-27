"""Task 2: Binary Search.

The input collection must be sorted in ascending order.
Time complexity: O(log n) worst case
Space complexity: O(1)
"""


def binary_search(collection, target):
    """Return the target's index, or -1 if it is not present."""
    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = (low + high) // 2

        if collection[mid] == target:
            return mid
        if target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
