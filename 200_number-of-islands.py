class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Time: O(V + E) = O(m x n)
        Space: O(m x n)
        where m, n are rows, cols
        '''
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # if out of bounds, return
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            # if grid[r][c] is water/visited, return
            if grid[r][c] == '0':
                return

            # mark as visited
            grid[r][c] = '0'

            shifts = [[-1,0],[1,0],[0,1],[0,-1]]
            for dr, dc in shifts:
                r2, c2 = r + dr, c + dc
                dfs(r2, c2)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands
