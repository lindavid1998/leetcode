class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(n) time
        # O(26) space for the hash table 
        l = 0
        r = 0
        N = len(s)

        charCount = defaultdict(int)  # char -> count
        maxFreq = 0
        res = 0

        while r < N:
            charCount[s[r]] += 1
            maxFreq = max(maxFreq, charCount[s[r]])
            while r - l - maxFreq >= k:
                charCount[s[l]] -= 1
                l += 1
                # no need to decrement maxFreq
                # we only overwrite res if new longest length found
                # which can only occur with a larger maxFreq 
            res = max(res, r - l + 1)
            r += 1
        
        return res
