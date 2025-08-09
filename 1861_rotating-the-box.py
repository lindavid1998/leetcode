class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        two pointers, grid rotation

        time: O(m * n)
        space: O(m * n)
        """

        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for row in boxGrid:
            # slide stones over
            r = len(row) # pointer to track where to move stones
            for l in range(len(row) - 1, -1, -1):
                c = row[l]
                # air, do nothing
                if c == '.':
                    continue
                # wall, move r to l
                if c == '*':
                    r = l
                else:
                    # stone, move stone to r - 1 and r = r - 1
                    row[l] = '.'
                    row[r - 1] = '#'
                    r -= 1
        
        # rotate
        new_grid = []

        # for each col, make a new row and append to new grid
        for c in range(cols):
            new_row = []

            for r in range(rows - 1, -1, -1):
                new_row.append(boxGrid[r][c])
            
            new_grid.append(new_row)

        return new_grid



