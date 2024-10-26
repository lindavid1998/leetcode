class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # O(len(num1) * len(num2)) or approximately O(log(num1) * log(num2))
        # two pointers

        res = 0
        N2 = len(num2)
        N1 = len(num1)

        for p2 in range(N2 - 1, -1, -1):
            for p1 in range(N1 - 1, -1, -1):
                tmp = (ord(num1[p1]) - ord('0')) * (ord(num2[p2]) - ord('0'))
                res += tmp * 10 ** (N1 - p1 - 1) * 10 ** (N2 - p2 - 1)
        
        return str(res)