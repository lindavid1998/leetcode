class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        n x n grid of 0, 1, 2s
        n is odd

        Y defined as two diagonals ending at center square, and then vertical going down to bottom
        all cells in Y have to be same value
        all cells not in Y have to be same value
        so end state only has two values

        return min num of operations to make Y on the grid

        number of cells in Y = n + n // 2
        n = 3, n + n // 2 = 3 + 1 = 4
        n = 5, n + n // 2 = 5 + 2 = 7

        get count of 0, 1, 2s in Y
        get count of 0, 1, 2s outside of Y

        you have the following combinations
        Y: 0, not Y: 1 
        Y: 0, not Y: 2
        Y: 1, not Y: 0
        Y: 1, not Y: 2
        and so on

        for each combination y_val, outside_val, calculate the number of operations needed:
            Y_ops = size of Y - count of y_val
            outside_Y_ops = grid size - size of Y - count of outside_val
            total ops = y_ops + outside_y_ops
            res = min(total_ops, res)
        save the minimum number

        time: O(n^2) to iterate and get counts of 0, 1, 2 inside and outside Y
        space: O(1), counts array are constant space
        """

        n = len(grid)

        middle = n // 2 

        def is_cell_in_y(i, j):
            """
            a cell is in Y if it is above the middle row and on the diagonal
            i.e. (i == j or i + j + 1 == n)
            OR
            at or below the middle row and in the middle column n//2
            """
            if i >= middle:
                if j == middle:
                    return True
                return False
            
            return i == j or i + j + 1 == n


        y_counts = [0, 0, 0] # counts for 0, 1, 2 
        outside_counts = [0, 0, 0] # counts for 0, 1, 2

        # iterate over grid and get count
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if is_cell_in_y(i, j):
                    y_counts[val] += 1
                else:
                    outside_counts[val] += 1

        y_size = n + n // 2
        grid_size = n * n
        res = float("inf")

        for y_val in range(3):
            for outside_val in range(3):
                if y_val == outside_val:
                    continue
                y_ops = y_size - y_counts[y_val]
                outside_ops = grid_size - y_size - outside_counts[outside_val]
                total_ops = y_ops + outside_ops
                res = min(total_ops, res)

        return res

