class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(2^n) DFS solution, TLE
	if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(m x n) time and space, DFS with cache
	# top down DP
	dp = {} # (m, n) -> unique paths
        def dfs(m, n):
            if (m, n) in dp:
                return dp[(m, n)]
            if m == 1 or n == 1:
                return 1
            
            dp[(m, n)] = dfs(m - 1, n) + dfs(m, n - 1)

            return dp[(m, n)]
            
        return dfs(m, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
	# O(m x n) time and space, bottom up DP
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                    continue

                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[m - 1][n - 1]

