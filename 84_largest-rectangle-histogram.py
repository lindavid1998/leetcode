class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        O(n) time and space

        use a stack to keep track of which bars can be extended to the right
        to make valid rectangles
        
        once a bar can't be extended, it is popped from the stack

        a bar can only be extended to the next bar that is shorter than it
        '''
        s = [] # (idx, height)
        N = len(heights)
        maxArea = 0

        for i in range(N):
            start = i
            while s and heights[i] < s[-1][1]:
                j, height = s.pop()
                area = (i - j) * height
                maxArea = max(area, maxArea)
                start = j  # each time we pop from stack, we can extend the i'th bar to the left
            s.append([start, heights[i]])
        
        while s:
            j, height = s.pop()
            area = (N - j) * height
            maxArea = max(area, maxArea)
        
        return maxArea

