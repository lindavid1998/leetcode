class Solution:
    def jump(self, nums: List[int]) -> int:
        # O(n)
        # build windows of indices that can be reached on each iteration
        # return the number of windows 
        res = 0
        l = 0
        r = 0
        N = len(nums)
        while r < N - 1:
            nxtR = r
            for i in range(l, r + 1):
                nxtR = max(nxtR, i + nums[i])
            l = r + 1 # next window will always start adjacent to prev
            r = nxtR # next window ends where it can reach the farthest
            res += 1

        return res
        
        # O(n^2)
        N = len(nums)
        g = N - 1
        count = 0

        # on each iteration
        # 1) move goal as far up as possible and 
        # 2) increment count by 1
        # repeat until goal is at front
        while g != 0:
            count += 1
            for i in range(g,-1,-1):
                if i + nums[i] >= g:
                    nxtG = i
            g = nxtG
            
        return count 