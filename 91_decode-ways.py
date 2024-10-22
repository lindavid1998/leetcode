class Solution:
    def numDecodings(self, s: str) -> int:
        # Iterative
        # O(len(s))
        n = len(s)
        dp = {n:1}

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]
            if i + 2 <= n and int(s[i:i+2]) < 27:
                dp[i] += dp[i + 2]

        return dp[0]
    
        # DFS with caching
        # O(len(s))
        N = len(s)
        dp = {N:1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            dp[i] = dfs(i + 1)
            if i + 1 < N and int(s[i:i+2]) < 27:
                dp[i] += dfs(i + 2)
            
            return dp[i]
        
        return dfs(0)
    
        # DFS without caching
        # O(2^n) where n is len(s)
        def dfs(s):
            if not s:
                return 1
            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            
            res = dfs(s[1:])
            if int(s[0:2]) < 27:
                res += dfs(s[2:])
            return res
        
        return dfs(s)