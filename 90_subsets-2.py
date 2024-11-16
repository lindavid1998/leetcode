class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Time: O(n * 2^n)
        Space: O(n)
        '''
        nums.sort()

        res = []
        s = []
        def dfs(i):
            if i == len(nums):
                res.append(s.copy())
                return
            
            s.append(nums[i])
            dfs(i + 1)
            s.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i)
        
        dfs(0)

        return res

