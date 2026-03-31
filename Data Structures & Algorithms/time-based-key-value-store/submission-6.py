class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.keys[key]:
            return ""

        values = self.keys[key]

        i , j, res = 0, len(values) - 1, ""
        while i <= j:
            mid = i + (j - i)//2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                i = mid + 1
            else:
                j = mid - 1

        return res
