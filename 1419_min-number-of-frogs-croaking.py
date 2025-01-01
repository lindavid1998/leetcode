class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        charCount = defaultdict(int)
        res = count = 0
        
        for char in croakOfFrogs:
            charCount[char] += 1
            if char == 'c':
                count += 1
                res = max(count, res)
            if char == 'k':
                count -= 1

            if charCount['c'] < charCount['r'] or \
                charCount['r'] < charCount['o'] or \
                charCount['o'] < charCount['a'] or \
                charCount['a'] < charCount['k']:
                return -1

        return res if count == 0 else -1