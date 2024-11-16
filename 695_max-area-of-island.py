class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Time: O(m x n)
        Space: O(m x n)
        '''
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            shifts = [[-1,0],[1,0],[0,1],[0,-1]]
            for dr, dc in shifts:
                r2, c2 = r + dr, c + dc
                area += dfs(r2, c2)
            return area

        for r in range(rows):
            for c in range(cols):
                area = dfs(r, c)
                maxArea = max(area, maxArea)

        return maxArea

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        BFS
        Time: O(m x n)
        Space: O(m x n)
        '''
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            area = 0
            q = deque()

            if grid[r][c] == 1:
                q.append((r,c))
                grid[r][c] = 0  # mark as visited

            while q:
                x, y = q.popleft()
                
                area += 1  

                shifts = [[-1,0],[1,0],[0,1],[0,-1]]
                for dx, dy in shifts:
                    x2, y2 = x + dx, y + dy
                    if x2 < 0 or y2 < 0 or x2 == ROWS or y2 == COLS:
                        continue
                    if grid[x2][y2] == 0:
                        continue
                    
                    grid[x2][y2] = 0
                    q.append((x2,y2))

            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = bfs(r, c)
                maxArea = max(area, maxArea)
        return maxArea

