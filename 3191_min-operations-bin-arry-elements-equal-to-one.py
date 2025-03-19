class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # Greedy, sliding window

        # Slide window to the right until end of array is reached
        # if first element of window is 0, flip the numbers in the array
        # any elements to the left of the window will always be equal to 1
        # so whether or not a solution is possible depends on the last 3 elements 

        count = 0
        l = 0
        r = 2
        n = len(nums)

        while r < n:
            if nums[l] == 0:
                for i in range(l, l + 3):
                    nums[i] = 1 if nums[i] == 0 else 0
                count += 1
            l += 1
            r += 1
        
        for i in range(n - 3, n):
            if nums[i] != 1:
                return -1
        
        return count
