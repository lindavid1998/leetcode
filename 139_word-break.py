class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        res = [False] * (N + 1)
        res[-1] = True

        for i in range(N - 1, -1, -1):
            for word in wordDict:
                l = len(word)
                
                if i + l < N + 1 and s[i:i + l] == word and res[i + l] == True:
                    res[i] = True
                    break
        
        return res[0]