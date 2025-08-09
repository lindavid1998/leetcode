def min_blocks(towers):
    """
    start with ascending
    assume towers starts at height s
    target[i] = s + i
    target has to be above or equal to tower[i], otherwise impossible
    i.e. s + i >= tower[i]
    rearranging for s, we get s >= tower[i] - i

    the optimal start is s = max(tower[i] - i)
    why? any less than that and the constraint s + i >= tower[i] will be broken

    to solve for ascending
    1. find starting height
    2. calculate targets
    3. sum difference to target for each index

    repeat for descending
    for descending, the constraint is s - i >= tower[i]
    i.e. s >= tower[i] + i or s = max(tower[i] + i)

    time: O(n)
    space: O(1)
    """
    n = len(towers)
    res = float("inf")

    # ascending
    start_asc = max(towers[i] - i for i in range(n))
    cost = 0
    for i in range(n):
        target = start_asc + i
        cost += target - towers[i]
    res = min(cost, res)

    # descending
    start_desc = max(towers[i] + i for i in range(n))
    cost = 0
    for i in range(n):
        target = start_desc - i
        cost += target - towers[i]
    res = min(cost, res)

    return res

# Tests
print(min_blocks([5, 7, 9, 4, 11]))  # 9
print(min_blocks([3, 2, 4, 2]))      # 7
print(min_blocks([5, 7, 14, 4, 11])) # 29
print(min_blocks([1, 2, 3, 4, 5]))   # 0
print(min_blocks([5, 4, 3, 2, 1]))   # 0
print(min_blocks([10, 1, 10, 1]))    # 20
print(min_blocks([1, 4, 5, 6]))      # 2
print(min_blocks([2, 4, 3, 2]))      # 3
print(min_blocks([1]))               # 0
