class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # bottom up DP
        # O(n x m) time and space

        N1 = len(s1)
        N2 = len(s2)

        if N1 + N2 != len(s3):
            return False
        
        dp = [[False for _ in range(N2 + 1)] for _ in range(N1 + 1)]
        dp[N1][N2] = True
        print(dp)
        for i in range(N1, -1, -1):
            for j in range(N2, -1, -1):
                if i < N1 and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < N2 and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
	# top down DP with memoization
	# O(n x m) time and space

        N1 = len(s1)
        N2 = len(s2)

        if N1 + N2 != len(s3):
            return False

        dp = {} # (i, j) -> True/False

        def dfs(i, j):
            if i == N1 and j == N2:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = False
            if i < N1 and s1[i] == s3[i + j]:
                dp[(i, j)] = dp[(i, j)] or dfs(i + 1, j)
            if j < N2 and s2[j] == s3[i + j]:
                dp[(i, j)] = dp[(i, j)] or dfs(i, j + 1)
            
            return dp[(i, j)]
        
        return dfs(0, 0)

