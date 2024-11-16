class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Time: O(n * 2^n)
        Space: O(n)
        '''
        candidates.sort()
        res = []
        s = []
        def dfs(i, total):
            if total == target:
                res.append(s.copy())
                return
            if total > target or i == len(candidates):
                return

            s.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            s.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            dfs(i, total)
        
        dfs(0, 0)

        return res

