#Task 1: Linear Search.

#Time complexity: O(n) worst case
#Space complexity: O(1)



def linear_search(collection, target):
    """Return the target's index, or -1 if it is not present."""
    for index, value in enumerate(collection):
        if value == target:
            return index
    return -1
