class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(m * n) time
        # O(m * n) space if including res[]

        # use pointers to define boundary of unvisited cells
        l = 0
        t = 0
        r = len(matrix[0]) - 1
        b = len(matrix) - 1

        res = []
        while l <= r and t <= b:
            # traverse all elements in top row
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1  # shrink boundary

            if t > b:
                break

            # traverse all elements in right col
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            if r < l:
                break

            # traverse all elements in bot row
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1

            # traverse all elements in left col
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res