class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time, # O(1) space

        N = len(nums)
        # iterate over nums to generate prefix
        res = [1] * N
        for i in range(1, N):
            res[i] = nums[i - 1] * res[i - 1]

        # iterate over nums in reverse to multiply by postfix
        postfix = 1
        for i in range(N - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
