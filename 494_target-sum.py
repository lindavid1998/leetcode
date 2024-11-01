class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # top down DP
        # O(len(nums) * target) time and space
        N = len(nums)
        dp = {}
        def dfs(i, total):
            if i == N:
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

            return dp[(i, total)]
        
        return dfs(0, 0)

# TODO: bottom up solution?