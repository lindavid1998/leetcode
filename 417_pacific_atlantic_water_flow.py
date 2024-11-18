class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        DFS, Time and space O(m x n)
        '''
        pac_set = set()
        atl_set = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, prev_height, visited):
            if r < 0 or c < 0 or r == rows or c == cols:
                return
            cur_height = heights[r][c]
            if cur_height < prev_height:
                return
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            
            dfs(r + 1, c, cur_height, visited)
            dfs(r - 1, c, cur_height, visited)
            dfs(r, c + 1, cur_height, visited)
            dfs(r, c - 1, cur_height, visited)

        # find all cells that can reach pacific
        # find all cells that can reach atlantic
        for c in range(cols):
            dfs(0, c, 0, pac_set)
            dfs(rows - 1, c, 0, atl_set)

        for r in range(rows):
            dfs(r, 0, 0, pac_set)
            dfs(r, cols - 1, 0, atl_set)

        # return the intersection of both sets
        res = []
        for (r, c) in pac_set:
            if (r, c) in atl_set:
                res.append([r, c])
        return res

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        BFS, O(m x n) time and space
        '''
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def bfs(r, c):
            q = deque()
            if board[r][c] == 'O':
                q.append([r, c])
                visited.add((r, c))

            while q:
                x, y = q.popleft()

                shifts = [[-1,0],[1,0],[0,1],[0,-1]]

                for dx, dy in shifts:
                    x2, y2 = x + dx, y + dy
                    if x2 < 0 or y2 < 0 or x2 == rows or y2 == cols:
                        continue
                    if (x2, y2) in visited:
                        continue
                    if board[x2][y2] == 'X':
                        continue
                    
                    visited.add((x2, y2))
                    q.append((x2, y2))

        for r in range(rows):
            for c in [0, cols - 1]:
                bfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:
                bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = 'X'

