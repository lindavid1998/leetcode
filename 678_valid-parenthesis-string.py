# O(n) greedy algorithm
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # leftMin and leftMax represent the number of unclosed parentheses at any given point
        # increment both when an "(" is found, decrement if ")"
        # since * is wild, we can decrement leftMin and increment leftMax

        leftMin = 0
        leftMax = 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            # we can terminate early if leftMax is negative since it'll be impossible to create valid string
            # ex: )))))() 
            if leftMax < 0:
                return False
            # if leftMin ever goes negative, reseting it to 0 means we can count some of the previous * as spaces instead
            if leftMin < 0:
                leftMin = 0
        
        # s is not valid if leftMax is negative (handled in the loop) or leftMin is positive
        return leftMin == 0

# O(n^2) DFS with cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        cache = {}
        def dfs(i, nOpen):
            if (i, nOpen) in cache:
                return cache[(i, nOpen)]
            if i == N:
                return nOpen == 0
            if nOpen < 0:
                cache[(i, nOpen)] = False
                return False
            
            if s[i] == '(':
                cache[(i, nOpen)] = dfs(i + 1, nOpen + 1)
            elif s[i] == ')':
                cache[(i, nOpen)] = dfs(i + 1, nOpen - 1)
            else:
                cache[(i, nOpen)] = dfs(i + 1, nOpen + 1) or dfs(i + 1, nOpen - 1) or dfs(i + 1, nOpen)
            
            return cache[(i, nOpen)]
        
        return dfs(0, 0)

# O(3^n) DFS without cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        def dfs(i, nOpen):
            if i == N:
                return nOpen == 0
            if nOpen < 0:
                return False
            
            if s[i] == '(':
                return dfs(i + 1, nOpen + 1)
            elif s[i] == ')':
                return dfs(i + 1, nOpen - 1)
            else:
                return dfs(i + 1, nOpen + 1) or dfs(i + 1, nOpen - 1) or dfs(i + 1, nOpen)
        
        return dfs(0, 0)