class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window
        O(n) time and space

        Expand the window until string is invalid
        Then shrink the window until there are no more duplicates in window
        '''
        res = 0
        l = 0
        r = 0
        chars = set()
        while r < len(s):
            # move left pointer while string has duplicate chars
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res
