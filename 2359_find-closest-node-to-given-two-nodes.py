class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        need to get shortest distance from node1 and node2 to their neighbors
        this can be done with bfs or dfs since unweighted and there is only 1 outgoing edge

        time: O(n) for DFS + O(n) to check which nodes are reachable from both nodes
        space: O(n) recursive depth for DFS, and the dist maps
        """
        def dfs(node, cur_distance, dist):
            if node == -1:
                # null node
                return
            if dist[node] != float("inf"):
                # node is visited already
                return
            
            dist[node] = cur_distance # shortest path to node found
            neighbor = edges[node]
            dfs(neighbor, cur_distance + 1, dist)
            return
        
        n = len(edges)
        dist1 = [float("inf")] * n  # mark all nodes as unvisited initially
        dist2 = [float("inf")] * n

        dfs(node1, 0, dist1)
        dfs(node2, 0, dist2)

        min_dist = float("inf")
        res = -1
        for i in range(n):
            if dist1[i] == float("inf") or dist2[i] == float("inf"):
                # node i is not reachable from both node1 and node2
                continue
            max_dist = max(dist1[i], dist2[i])
            if max_dist < min_dist:
                min_dist = max_dist
                res = i
        return res


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            dist_map = {}
            q = deque()
            q.append(start)
            dist = 0
            while q:
                node = q.popleft()
                dist_map[node] = dist
                if edges[node] != -1 and edges[node] not in dist_map:
                    q.append(edges[node])
                dist += 1
            return dist_map

        node1_dist_map = bfs(node1)
        node2_dist_map = bfs(node2)

        res = -1
        min_dist = float("inf")

        for dest in node1_dist_map.keys():
            if dest in node2_dist_map:
                max_dist = max(node1_dist_map[dest], node2_dist_map[dest])
                if max_dist == min_dist and dest < res:
                    res = dest # return the smaller index
                if max_dist < min_dist:
                    min_dist = max_dist
                    res = dest

        return res
