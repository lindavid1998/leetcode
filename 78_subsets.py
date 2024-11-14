class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []
        def dfs(i):
            if i == len(nums):
                res.append(s.copy())
                return
            
            s.append(nums[i])
            dfs(i + 1)
            s.pop()
            dfs(i + 1)
        
        dfs(0)

        return res
            
