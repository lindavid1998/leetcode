class CountSquares:
    # O(n) time and space

    def __init__(self):
        # track points and their count
        self.points = []
        self.ptsCount = defaultdict(int) # (x, y) -> count

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # first look for the diagonal point with equal delta_x and delta_y
        # once found, look for the other two points inside the ptsCount dict
        px, py = point
        res = 0

        for x, y in self.points:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            res += self.ptsCount[(px, y)] * self.ptsCount[(x, py)]

        return res        

