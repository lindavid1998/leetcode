class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        greedy
        always include 0s
        include 1 bits starting from least significant, add 
        only if including it doesn't exceed k

        time: O(n)
        space: O(1)
        """
        zeros = s.count('0')
        ones = 0
        value = 0
        multiplier = 1

        n = len(s)
        for i in range(n - 1, -1, -1):
            bit = s[i]
            if bit == "1":
                if value + multiplier <= k:
                    ones += 1
                    value += multiplier
            multiplier *= 2
            if multiplier > k:
                break

        return zeros + ones

