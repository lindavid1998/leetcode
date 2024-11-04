class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        O(n) time, O(1) space
        two pointers starting at opposite ends
        traverse inwards
        at each step, calc area that can be collected and overwrite max
        move pointer that has the smaller height
        '''

        maxArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            
            maxArea = max(maxArea, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
