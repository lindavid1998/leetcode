class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        O(n) time, O(1) space
        two pointers
        init left and right on opposite ends and traverse inwards until array is traversed
        at any point, height contribution from left and right pointer can be calculated

        height contribution from idx i = min(maxLeft, maxRight) - height[i]

        since at each i we care only about min between maxLeft and maxRight, we can calculate
        the height contribution from the left pointer if maxLeft < maxRight

        likewise, we can do the same for the right pointer if maxRight >= maxLeft
        '''

        l = 0
        r = len(height) - 1
        leftMax = height[0]
        rightMax = height[r]

        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time and space
        # prefix and suffix arrays

        N = len(height)
        maxLefts = [0] * N
        maxRights = [0] * N

        for i in range(1, N):
            maxLefts[i] = max(height[i - 1], maxLefts[i - 1])

        for i in range(N - 2, -1, -1):
            maxRights[i] = max(height[i + 1], maxRights[i + 1])
    
        res = 0
        for i in range(N):
            tmp = min(maxLefts[i], maxRights[i]) - height[i]
            res += max(0, tmp)
        
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n^2) brute force, O(1) space
        N = len(height)
        res = 0

        for i in range(N):
            # get left max
            leftMax = 0
            for j in range(i - 1, -1, -1):
                leftMax = max(leftMax, height[j])
            # get right max
            rightMax = 0
            for j in range(i + 1, N):
                rightMax = max(rightMax, height[j])
            
            tmp = min(leftMax, rightMax) - height[i]
            if tmp > 0:
                res += tmp
        return res
