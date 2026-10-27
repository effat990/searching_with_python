

from task1_linear_search import linear_search
from task2_binary_search import binary_search
from task3_search_comparison import (
    count_linear_search_steps,
    count_binary_search_steps,
)


# Do Not Modify This Section
def main():
    print("TEST 1")
    data = [3, 7, 12, 18, 21, 25, 31, 40, 44, 52]
    target = 25
    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print("TEST 2")
    data = [1, 2, 3, 4, 5]
    target = 1
    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print("TEST 3")
    data = [1, 2, 3, 4, 5]
    target = 5
    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print("TEST 4")
    data = [1, 2, 3, 4, 5]
    target = 10
    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print("TEST 5")
    data = []
    target = 5
    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))


if __name__ == "__main__":
    main()
