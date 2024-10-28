class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # O(2^n)
        res = []
        def dfs(nOpen, nClose, s):
            if nOpen > n or nClose > n:
                return
            if nOpen < nClose:
                return
            if nOpen == n and nClose == n:
                res.append(s)
                return

            dfs(nOpen + 1, nClose, s + '(')
            dfs(nOpen, nClose + 1, s + ')')
    
        dfs(0, 0, "")
        
        return res
