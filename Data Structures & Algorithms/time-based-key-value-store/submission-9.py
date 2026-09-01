from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([], [])

        timestamps, values = self.store[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        timestamps, values = self.store[key]
        index = bisect_right(timestamps, timestamp) - 1

        if index < 0:
            return ""

        return values[index]