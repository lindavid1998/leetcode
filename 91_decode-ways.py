class Solution:
    def numDecodings(self, s: str) -> int:
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
    
        # Recursive solution
        n = len(s)
        dp = {n:1}

        def helper(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = helper(i + 1)
            if i + 2 <= n and int(s[i:i+2]) < 27:
                res += helper(i + 2)
            
            dp[i] = res
            return res
        
        return helper(0)