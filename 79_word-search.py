class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        DFS, backtracking
        Time: O(m x 4^n)
        Space: O(n)
        where n is the length of the word
        '''
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if board[i][j] != word[idx]:
                return False
            
            # mark letter as visited
            tmp = board[i][j]
            board[i][j] = '#'

            shifts = [[-1,0],[1,0],[0,1],[0,-1]]
            for dx, dy in shifts:
                i2 = i + dx
                j2 = j + dy
                if dfs(i2, j2, idx + 1):
                    return True
            
            # unmark letter as visited (backtrack)
            board[i][j] = tmp
            
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
