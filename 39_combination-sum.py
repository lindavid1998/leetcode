class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = []
        res = []
        def dfs(i, total):
            if total == target:
                res.append(s.copy())
                return
            if total > target or i == len(nums):
                return
            
            s.append(nums[i])
            dfs(i, total + nums[i])
            s.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        
        return res
