"""Task 3: Compare Linear Search and Binary Search.

Counts comparisons made by each algorithm.
Linear Search: O(n) worst-case time, O(1) extra space.
Binary Search: O(log n) worst-case time, O(1) extra space; sorted input required.
"""

from task1_linear_search import linear_search
from task2_binary_search import binary_search


def count_linear_search_steps(collection, target):
    """Count element-to-target comparisons made by Linear Search."""
    steps = 0
    for value in collection:
        steps += 1
        if value == target:
            break
    return steps


def count_binary_search_steps(collection, target):
    """Count comparisons with middle elements made by Binary Search."""
    low = 0
    high = len(collection) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        steps += 1

        if collection[mid] == target:
            break
        if target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return steps


def compare_searches(collection, target):
    """Return search results and comparison counts for both algorithms."""
    return {
        "linear_search_index": linear_search(collection, target),
        "binary_search_index": binary_search(collection, target),
        "linear_search_steps": count_linear_search_steps(collection, target),
        "binary_search_steps": count_binary_search_steps(collection, target),
    }


if __name__ == "__main__":
    data = [3, 7, 12, 18, 21, 25, 31, 40, 44, 52]
    target = 25
    print("Task 3: Search Comparison")
    for label, result in compare_searches(data, target).items():
        print(f"{label}: {result}")
