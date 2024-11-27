class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) time, O(1) space
        N = len(nums)
        if N < 3:
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, N):
            nums[i] = max(nums[i-1], nums[i] + nums[i-2])
        
        return nums[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Top down DP
        O(n) time and space
        '''
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(nums):
                return 0
            
            dp[i] = max(
                dfs(i + 1),
                dfs(i + 2) + nums[i]
            )

            return dp[i]
        return dfs(0)
