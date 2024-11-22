class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
	'''
	Time: O(n + E*a(n))
	Space: O(n)
	where E is the number of edges and n is number of nodes
	a(n) is amortized cost, which is near constant 
	'''
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

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for nxt in adjList[i]:
                dfs(nxt)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

