class Solution:
    def solveNQueens(self, n):
        visited = set()
        stack = []
        res = []

        def dfs(i):
            if i == n:
                res.append(stack.copy())
                return
            
            for j in range(n):
                if j in visited: continue

                visited.add(j)
                stack.append([i, j])
                dfs(i + 1)
                visited.remove(j)
                stack.pop()


        dfs(0)

        return res
solution = Solution()
print(solution.solveNQueens(1))
print(solution.solveNQueens(2))
print(solution.solveNQueens(3))
print(solution.solveNQueens(4))
