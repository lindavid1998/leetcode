class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        Top down DP with memoization
        Time: O(n * m)
        Space: O(n * m)
        '''
        n, m = len(matrix), len(matrix[0])

        dp = {} # (r, c) -> lip
        def dfs(r, c, prev):
            if r < 0 or c < 0 or r == n or c == m:
                return 0
            if matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1

            next_lip = 0
            next_lip = max(next_lip, dfs(r + 1, c, matrix[r][c]))
            next_lip = max(next_lip, dfs(r - 1, c, matrix[r][c]))
            next_lip = max(next_lip, dfs(r, c + 1, matrix[r][c]))
            next_lip = max(next_lip, dfs(r, c - 1, matrix[r][c]))

            res += next_lip

            dp[(r, c)] = res
            
            return res
        
        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, dfs(r, c, -1))

        return res
