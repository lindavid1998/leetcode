class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # key intuition 1: a and b can never equal each other
        # if a % x != b % x

        # key intuition 2: min operations is determined by the median
        # median by definition minimizes the sum of absolute differences
        # minimizing sum of absolute differences will in turn minimize
        # the number of operations needed

        # Time: O(nlogn)
        # Space: O(n)

        n_rows = len(grid)
        n_cols = len(grid[0])
        remainder = grid[0][0] % x
        nums = []
        for r in range(n_rows):
            for c in range(n_cols):
                num = grid[r][c]
                
                if num % x != remainder:
                    return -1
                
                nums.append(num)
        
        # get median
        nums.sort()
        median = nums[len(nums) // 2]

        # count operations
        count = 0
        for n in nums:
            count += abs(median - n) // x

        return count
