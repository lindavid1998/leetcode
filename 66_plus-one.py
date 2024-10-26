class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # O(n) time, O(1) space
        increment = 1
        N = len(digits)
        for i in range(N - 1, -1, -1):
            newDigit = digits[i] + increment
            digits[i] = newDigit % 10
            if newDigit < 10:
                return digits
        
        digits.insert(0, 1)
        return digits