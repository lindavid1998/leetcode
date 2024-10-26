class Solution:

    def encode(self, strs: List[str]) -> str:
        # O(n)
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        # O(n)
        res = []
        l = 0
        r = 0
        while l < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            res.append(s[r + 1:r + length + 1])
            l = r + length + 1
            r = l
        return res
