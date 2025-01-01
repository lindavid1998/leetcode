class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        res = [False] * (N + 1)
        res[-1] = True

        for i in range(N - 1, -1, -1):
            for word in wordDict:
                l = len(word)
                
                if i + l < N + 1 and s[i:i + l] == word and res[i + l] == True:
                    res[i] = True
                    break
        
        return res[0]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            
            dp[i] = False
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                if s[i:i + len(word)] == word and dfs(i + len(word)):
                    dp[i] = True

            return dp[i]
        
        return dfs(0)
