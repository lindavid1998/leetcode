class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) time
        N = len(s)
        res = s[0]
        maxLen = 0

        for i in range(N):
            # odd palindrome lengths
            l = i
            r = i
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # even palindrome
            l = i
            r = i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res