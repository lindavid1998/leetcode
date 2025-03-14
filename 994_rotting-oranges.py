class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        BFS
        Time: O(m x n)
        Space: O(m x n)
        add rotten fruits to queue
        while there are rotten fruits and fresh fruits remaining, process queue
        '''
        ROWS = len(grid)
        COLS = len(grid[0])

        num_fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        minutes = 0
        while num_fresh > 0 and q:
            # if num_fresh > 0 is left out, then you end up with an extra minute
            # the last rotten fruits end up in queue, and another minute is spent popping them
            # even though there are no more fresh fruits left
            n = len(q)
            for _ in range(n):
                x,y = q.popleft()
                shifts = [[1,0],[-1,0],[0,1],[0,-1]]
                for dx,dy in shifts:
                    x2,y2 = x + dx, y + dy
                    if x2 < 0 or y2 < 0 or x2 == ROWS or y2 == COLS:
                        continue
                    if grid[x2][y2] == 1:
                        grid[x2][y2] = 2
                        q.append((x2,y2))
                        num_fresh -= 1
            minutes += 1

        return minutes if num_fresh == 0 else -1
