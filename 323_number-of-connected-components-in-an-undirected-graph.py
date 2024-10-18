class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]  # path compression
                res = par[res]

            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        res = n
        for a,b in edges:
            if union(a,b):
                # each union reduces num of connected components by 1
                res -= 1
        return res