class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(n)
        # loop from back to front
        # if cell can reach goal, move goal to cell
        N = len(nums)
        G = N - 1
        for i in range(N-2,-1,-1):
            if i + nums[i] >= G:
                G = i
        
        return G == 0
        
        # O(n^2)
        N = len(nums)
        res = [False] * N
        res[-1] = True

        for i in range(N-1,-1,-1):
            for j in range(i,i + nums[i] + 1):
                if res[j] == True:
                    res[i] = True
                    break
        
        return res[0]