class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # each nums[i] can either extend subarray or start new one
        # curMin and curMax represent min and max of subarray that includes nums[i]
        res = nums[0]
        curMin = 1
        curMax = 1

        for n in nums:
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            res = max(res, curMax)

        return res