class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        hash map

        time: O(n + dlogd) where n is number of elements and d is number
        of diagonals
        diagonals should be O(rows + cols)

        space: O(n) for the hash map
        """
        diagonals = defaultdict(list)
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonals[r + c].append(nums[r][c])
        
        # O(dlogd) where d is number of diagonals
        # d = rows + cols
        sorted_keys = sorted(diagonals.keys())

        # O(n)
        res = []
        for key in sorted_keys:
            res += reversed(diagonals[key])
        return res

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        sorting

        key intuition is that all numbers (i, j) in diagonal have the same
        sum i + j. also for each diagonal, we traverse numbers in order of decreasing
        row

        we can iterate over nums and create an array of tuples
        (sum, row, value). then we can sort by sum and row to get the order of values

        time: O(nlogn) where n is total number of elements in nums
        space: O(n)
        """
        sum_row_val = []
        for i, row in enumerate(nums):
            for j in range(len(row)):
                val = nums[i][j]
                _sum = i + j
                sum_row_val.append((_sum, i, val)) # sum, row, value
        
        # sort 
        # by sum (ascending), row (descending)
        sum_row_val.sort(key = lambda x: (x[0], -x[1]))

        # return values in arr
        res = [val for s, r, val in sum_row_val]
    
        return res

