class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        I initially approached this with Djikstra's but it gives the wrong answer because we have to consider
        number of stops. We need to consider more expensive paths with less stops as these can be cheaper overall

        Can solve this problem with BFS where each layer corresponds to the number of stops
        Continue exploring from a node if 1) cheaper price found and 2) number of stops is not violated

        Time: O(k * (n + m)) where m is length of flights
        BFS is O(V + E) but that's with visitng each node and edge just once. Here we can explore each up to k times
        Space: O(m + n*k)
        - adjList is O(m)
        - prices is O(n)
        - queue is O(n * k), Normally for BFS space is O(V) but since we can visit each node up to k times,
        space is actually n * k
        """
        adjList = [[] for _ in range(n)]
        for frm, to, cost in flights:
            adjList[frm].append([to, cost])
        
        q = deque()

        prices = [float("inf")] * n
        prices[src] = 0

        q.append([src, 0, 0]) # node, cumulative price, num stops

        while q:
            node, price, num_stops = q.popleft()
            if num_stops > k:
                continue
            
            neighbors = adjList[node]
            for neighbor, cost in neighbors:
                new_price = price + cost
                if new_price < prices[neighbor]:
                    prices[neighbor] = new_price
                    q.append([neighbor, new_price, num_stops + 1])
        
        return prices[dst] if prices[dst] != float("inf") else -1

