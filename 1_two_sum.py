class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i, n in enumerate(nums):
            other = target - n
            if other in numToIndex:
                return [numToIndex[other], i]
            numToIndex[n] = i

