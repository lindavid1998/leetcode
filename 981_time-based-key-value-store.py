class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list) # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # O(log n)
        res = ""
        values = self.cache[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

