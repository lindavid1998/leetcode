class Solution:
    def climbStairs(self, n: int) -> int:
        # O(1) space
        if n <= 3:
            return n

        n1 = 1
        n2 = 2

        for i in range(3, n + 1):
            tmp = n1 + n2
            n1 = n2
            n2 = tmp 

        return tmp
    
        # O(n) space
        # if n == 1:
        #     return 1
            
        # res = [0] * (n + 1)
        # res[1] = 1
        # res[2] = 2
        # for i in range(3, n + 1):
        #     res[i] = res[i - 2] + res[i - 1]
        # return res[n]