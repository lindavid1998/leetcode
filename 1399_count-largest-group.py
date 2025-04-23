class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        dp = { 0:0 } # maps num to sum of digits
        
        counts = [0] * (9 * 4) 
        # n <= 10^4 so max digit sum is 36 (9999)
        # counts[i] -> size of group with digit sum of i + 1
        
        for i in range(1, n + 1):
            # get the sum of digits
            a, b = divmod(i, 10)
            dp[i] = b + dp[a]

            # update counts[]
            counts[dp[i] - 1] += 1
        
        largest = max(counts)
        count = 0
        for c in counts:
            if c == largest:
                count += 1
        return count

