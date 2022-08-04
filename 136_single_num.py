# Given a non-empty array of integers nums, every element appears twice except for one.\
# Find that single one.

# You must implement a solution with a linear runtime complexity
# and use only constant extra space.
 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

class Solution(object):
    def findSingleNum(self, nums):
        # Input: nums -> non empty array of integers
        # Output: integer

        # if nums is size 1, return single element
        if len(nums) == 1:
            return nums[0]

        numsCount = {}

        # iterate over array
        for num in nums:
        # if num is in dictionary, add 1 to count
        # otherwise, initialize count as 1
            if numsCount.get(num) != None:
                numsCount[num] += 1
            else:
                numsCount[num] = 1

        # return key with lowest value
        return min(numsCount, key=numsCount.get)


def assertEqual(actual, expected):
    if actual == expected:
        print('passed')
    else:
        print(f'failed. expected {expected} but got {actual}')

input = [2, 2, 1]
assertEqual(Solution().findSingleNum(input), 1)

input = [4, 1, 2, 1, 2]
assertEqual(Solution().findSingleNum(input), 4)

input = [1]
assertEqual(Solution().findSingleNum(input), 1)