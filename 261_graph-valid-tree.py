class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        DFS
        Time: O(V + E)
        Space: O(V + E), driven by adjacency list
            Recursive depth and visited set is O(V)
        '''
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        def dfs(node, prev_node):
            if node in visited:
                return False
            
            visited.add(node)
            for nxt in adjList[node]:
                if nxt == prev_node:
                    continue
                
                if dfs(nxt, node) == False:
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        BFS
        '''
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        q = deque()

        q.append([0, -1]) # [node, prev_node]
        visited.add(0) 

        while q:
            [node, prev_node] = q.popleft()
            for nxt in adjList[node]:
                if nxt == prev_node: continue
                if nxt in visited:
                    return False
                visited.add(nxt)
                q.append([nxt, node])
        
        return len(visited) == n
