class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.par = [i for i in range(size)]

    def find(self, i):
        # returns root parent of i
        p = self.par[i]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, i, j):
        # returns T if success, F otherwise
        p_i = self.find(i)
        p_j = self.find(j)

        if p_i == p_j:
            return False
        
        rank_i = self.rank[p_i]
        rank_j = self.rank[p_j]

        if rank_i >= rank_j:
            self.rank[p_i] += rank_j
            self.par[p_j] = p_i
        else:
            self.rank[p_j] += rank_i
            self.par[p_i] = p_j
        
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Union find 

        Time: O(n^2)
        Space: O(n^2) for the rank and parent arrs
        """
        n = len(grid)
        size = n * n

        def cell_index(i, j):
            return i * n + j

        union_find = UnionFind(size)

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        """
        iterate over grid. for every 1 found, check its neighbors. if any of its neighbors are land, join them
        """
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        i2, j2 = i + di, j + dj
                        if i2 < 0 or j2 < 0 or i2 >= n or j2 >= n:
                            # out of bounds
                            continue
                        if grid[i2][j2] == 1:
                            idx_1 = cell_index(i, j)
                            idx_2 = cell_index(i2, j2)
                            union_find.union(idx_1, idx_2)
        
        # init res with the largest island
        res = 0
        for area in union_find.rank:
            res = max(res, area)
        
        """
        iterate over grid
        when water is found, check its neighbors. if any of them are 1 and belongs to a new island, add its area
        save area if new max found
        """
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    seen_roots = set()
                    for di, dj in directions:
                        i2, j2 = i + di, j + dj
                        if i2 < 0 or j2 < 0 or i2 >= n or j2 >= n:
                            # out of bounds
                            continue

                        idx = cell_index(i2, j2)
                        root = union_find.find(idx)
                        if grid[i2][j2] == 1 and root not in seen_roots:
                            # new island found
                            area += union_find.rank[root] # add the size of the island
                            seen_roots.add(root) # mark as visited

                    res = max(res, area)
        return res
