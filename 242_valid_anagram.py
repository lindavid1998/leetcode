class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChars = defaultdict(int)
        tChars = defaultdict(int)
        
        for i in range(len(s)):
            sChars[s[i]] += 1
            tChars[t[i]] += 1
        
        return sChars == tChars

