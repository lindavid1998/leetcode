class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        target = []

        for i in range(n):
            # insert at index index[i] the value nums[i] in the target array
            idx = index[i]
            val = nums[i]

            target.insert(idx, val)

        return target