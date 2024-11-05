class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        O(n^2) time and space 
        Use hash table to track set of numbers in each row, column,
        and square

        Iterate over grid. Grid is invalid if duplicates found
        '''
        numRows = 9
        numCols = 9

        rows = defaultdict(set) # idx -> set
        cols = defaultdict(set) # idx -> set
        boxes = defaultdict(set) # i,j -> set

        for i in range(numRows):
            for j in range(numCols):
                n = board[i][j]

                if n == '.': continue

                if n in rows[i] or n in cols[j]:
                    return False
                if n in boxes[(i//3, j//3)]:
                    return False

                rows[i].add(n)
                cols[j].add(n)
                boxes[(i//3,j//3)].add(n)

        return True

