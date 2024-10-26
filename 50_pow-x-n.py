class Solution:
    def myPow(self, x: float, n: int) -> float:
        # O(log n)
        # 2^8 = (2 * 2 * 2 * 2) * (2 * 2 * 2 * 2)
        # 2^8 = 2^4 * 2^4 = 4^4
        # 4^4 = (4 * 4) * (4 * 4) = 4^2 * 4^2 = 16^2
        # 16^2 = 256^1
        def helper(x, n):
            # assume n is positive 
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))

        return res if n > 0 else 1 / res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # O(n) TLE
        if x == 0: return 0
        if n == 0: return 1
        
        res = 1.0
        for i in range(abs(n)):
            res *= x
        
        return res if n > 0 else 1 / res