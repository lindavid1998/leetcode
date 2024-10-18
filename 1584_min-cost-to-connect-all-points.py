class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2) + abs(y1-y2)
        
        # build adj list
        N = len(points)
        adjList = defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                dist = manhattan(points[i], points[j])
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        # prim's algo to find minimum spanning tree
        res = 0
        visited = set()
        heap = adjList[0]  # add all edges from source to heap
        visited.add(0)  # mark source as visited

        heapq.heapify(heap)
        while heap and len(visited) < N:
            d, i = heapq.heappop(heap)
            if i not in visited:
                visited.add(i)
                res += d
                for edge in adjList[i]:
                    heapq.heappush(heap, edge)
        
        return res

