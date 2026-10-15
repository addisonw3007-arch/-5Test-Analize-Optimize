# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return max(counts, key=counts.get)

print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # 3
print(most_frequent([5, 5, 2, 2]))           # 5 or 2
print(most_frequent([7]))                    # 7
print(most_frequent([]))                     # None

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A dictionary keeps track of how many times each number appears.
- Could it be optimized? This is already efficient because it only goes through the list once to count the numbers.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1]))           # [1]
print(remove_duplicates([]))                  # []
print(remove_duplicates([1, 2, 3]))           # [1, 2, 3]

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A set tracks which numbers have already appeared, while a list keeps them in their original order.
- Could it be optimized? Using a set is more efficient than repeatedly searching through a list.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        difference = target - num

        if difference in seen:
            pairs.append((difference, num))

        seen.add(num)

    return pairs

print(find_pairs([1, 2, 3, 4], 5))  # [(2, 3), (1, 4)]
print(find_pairs([1, 2, 3], 10))    # []
print(find_pairs([], 5))            # []
print(find_pairs([1, 4], 5))        # [(1, 4)]

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A set helps find matching numbers without using nested loops.
- Could it be optimized? This is already efficient because each number only needs to be checked once.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    size = 0
    items = [None] * capacity

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print("Resizing from", capacity, "to", new_capacity)

            new_items = [None] * new_capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            capacity = new_capacity

        items[size] = i + 1
        size += 1

    return items[:size]

print(add_n_items(6))
print(add_n_items(0))
print(add_n_items(2))
print(add_n_items(10))

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizing happens when the list reaches its maximum capacity. The capacity doubles each time it fills up
- What is the worst-case for a single append? O(n), because the program must create a larger list and copy all the existing elements into it.
- What is the amortized time per append overall? O(1), because most elements are added without resizing. The occasional expensive resize is spread across many additions.
- Space complexity: O(n), because the list grows as more elements are added.
- Why does doubling reduce the cost overall? Doubling the capacity means the program does not have to resize every time a new element is added. This saves time because resizing happens less frequently
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []

    for num in nums:
        total += num
        result.append(total)

    return result

print(running_total([1, 2, 3, 4]))  # [1, 3, 6, 10]
print(running_total([5, 5, 5]))     # [5, 10, 15]
print(running_total([]))            # []
print(running_total([10]))          # [10]
print(running_total([-1, 2, -3]))  # [-1, 1, -2]

"""
Time and Space Analysis for problem 5:
- Best-case: The function goes through each number once to calculate the running total.
- Worst-case: Even with a large list, the function only needs to go through each number once.
- Average-case: The time increases as the number of elements increases.
- Space complexity: A new list is created to store the running totals.
- Why this approach? Using a running total is easier and faster than adding all the previous numbers again for each position.
- Could it be optimized? This is already efficient because it only uses one loop. Memory could be reduced by modifying the original list, but that would change the input.
"""
