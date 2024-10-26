class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(m x n) time, O(1) space
        rows = len(matrix)
        cols = len(matrix[0])

        # iterate over matrix and mark rows and cols to change
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for i in range(cols):
                        matrix[r][i] = '#' if matrix[r][i] != 0 else 0
                    for i in range(rows):
                        matrix[i][c] = '#' if matrix[i][c] != 0 else 0

        # iterate over matrix again and convert all marked cells to 0s
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '#':
                    matrix[r][c] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(m x n) time and space

        nRows = len(matrix)
        nCols = len(matrix[0])
        rows = set()
        cols = set()

        # iterate over matrix to find rows and cols to change
        for r in range(nRows):
            for c in range(nCols):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        # change all the rows
        for r in rows:
            for c in range(nCols):
                matrix[r][c] = 0
        
        # change all the cols
        for c in cols:
            for r in range(nRows):
                matrix[r][c] = 0
        