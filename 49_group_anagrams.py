class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getAnagram(s):
            res = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                res[idx] += 1
            return tuple(res)
        
        res = {} # anagram -> word list
        for s in strs:
            anagram = getAnagram(s)
            if anagram not in res:
                res[anagram] = []
            res[anagram].append(s)
        
        return list(res.values())
        
