class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Time: O(n * 2^n)
        there are 2^n possible partitions because each char can either
        start a new partition or extend it
        Then for each partition, each substring has to be checked if it is
        a palindrome, which is an O(n) operation

        Space: O(n)
        '''
        def is_pal(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        part = [] # stack containing partitions

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if is_pal(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)

        return res


