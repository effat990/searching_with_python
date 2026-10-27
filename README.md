# Week 02 — Searching Algorithms



## Task 1 — Linear Search

Linear Search checks each element from the beginning until the target is found or all elements have been checked. It returns the target's zero-based index, or `-1` if the target is absent.

*Time complexity:* `O(n)` worst case
*Space complexity:* `O(1)`

# Task 2 — Binary Search

Binary Search requires a sorted collection. It compares the target with the middle element and continues searching in the left or right half until the target is found or the range becomes empty. It returns the target's zero-based index, or `-1` if absent.

*Time complexity:* `O(log n)` worst case
*Space complexity:* `O(1)` for the iterative implementation

# Task 3 — Compare Search Performance
This task compares the two search strategies and counts how many target comparisons each makes. The count is the number of elements/middle elements checked, not elapsed time.

*Linear Search:* checks sequentially; works on sorted or unsorted collections.
*Binary Search:* halves the range; requires sorted data.
*Worst-case time:* Linear Search `O(n)`; Binary Search `O(log n)`.
*Extra space:* both implementations use `O(1)`.

# Learning reflection

Linear Search examines elements one at a time, whereas Binary Search discards half of the remaining search range after each comparison. Binary Search can therefore use fewer comparisons on a large sorted collection, but it cannot be used directly on unsorted data. The comparison task makes this difference visible through step counts.

