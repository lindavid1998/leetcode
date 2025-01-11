class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        Time: O(n * m)
        Space: O(n * m)
        where n = len(s) and m = len(t)
        '''
        if len(t) > len(s):
            return 0

        dp = {}

        def dfs(i, j):
            # returns num of distinct subsequences of s[i:] such that it matches t[j:]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = dfs(i + 1, j) # num subsequences of s[i + 1:] to t[j:]
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            dp[(i, j)] = res
            
            return res
        
        return dfs(0, 0)
