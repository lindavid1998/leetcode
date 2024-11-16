class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        BFS

        Start by enqueuing all the treasure locations
        Process them in waves, incrementing distance each time
        Keep adding new land cells to queue

        Time: O((m x n)^2)
            It is possible to iterate over entire grid and enqueue each cell
            Then have to pop each cell from queue again
        Space: O(m x n)
        '''
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        dist = 1
        while q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                shifts = [[-1,0],[1,0],[0,1],[0,-1]]
                for dx, dy in shifts:
                    x2, y2 = x + dx, y + dy
                    if x2 < 0 or y2 < 0 or x2 == ROWS or y2 == COLS:
                        continue
                    if grid[x2][y2] == (2 ** 31) - 1:
                        grid[x2][y2] = dist
                        q.append((x2,y2))
            dist += 1
        
