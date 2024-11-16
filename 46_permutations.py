class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Time: O(n * n!)
        Space: O(n)
        '''
        res = []
        s = []
        used = set()
        def dfs():
            if len(s) == len(nums):
                res.append(s.copy())
                return
            
            for n in nums:
                if n not in used:
                    s.append(n)
                    used.add(n)
                    dfs()
                    s.pop()
                    used.remove(n)
        
        dfs()
        
        return res
