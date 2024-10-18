class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) time, O(1) space
        N = len(nums)

        if N < 3:
            return max(nums)

        def helper(l, r):
            rob1 = 0
            rob2 = 0

            for i in range(l, r):
                n = nums[i]
                tmp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = tmp

            return tmp
        
        # problem reduces to house robber I
        res = max(
            helper(0, N - 1), 
            helper(1, N)
        )
        
        return res
        