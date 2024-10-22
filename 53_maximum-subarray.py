class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n)
        # each num in nums can either extend subarray or start a new one
        res = float("-inf")
        curSum = 0

        for n in nums:
            curSum = max(n, curSum + n)
            res = max(res, curSum)

        return res