class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary search
        O(log(n * m))
        '''
        # find the row target could be in
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break # correct row found at m

        row = matrix[(top + bot) // 2]
        
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True

            if row[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

