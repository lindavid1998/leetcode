class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
	# O(len(text1)*len(text2)) time and space
	# bottom up DP
        N1 = len(text1)
        N2 = len(text2)

        dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]

        for i in range(N1 - 1, -1, -1):
            for j in range(N2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
	# O(len(text1) * len(text2)) time and space
	# top down DP with memoization
        N1 = len(text1)
        N2 = len(text2)

        dp = {} # (i, j) -> lcs
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == N1 or j == N2:
                return 0
            
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                res1 = dfs(i + 1, j)
                res2 = dfs(i, j + 1)
                dp[(i, j)] = max(res1, res2)

            return dp[(i, j)]
        
        return dfs(0, 0)
