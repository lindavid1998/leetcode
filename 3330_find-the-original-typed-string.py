class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        sliding window

        intuition: any string of repeated chars can be counted as possible strings
        example "abcccc" -> c, cc, ccc -> the substring "cccc" contributes 3 possible strings

        repeat until entire word is traversed:
        expand window to get length of repeating chars
        add length of window - 1 to res
        reset window
        """
        res = 0
        l = r = 0
        n = len(word)
        while r < n:
            while r < n and word[l] == word[r]:
                r += 1
            res += r - l - 1
            l = r
        return res + 1 # add 1 for the original string
