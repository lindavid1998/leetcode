class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        res = []
        visited = set()
        cycle = set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            
            cycle.add(i)
            for p in prereqs[i]:
                if dfs(p) == False:
                    return False
            cycle.remove(i)
            
            visited.add(i)
            res.append(i)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
