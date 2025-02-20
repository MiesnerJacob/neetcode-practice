from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        value_timestamps = self.hash_map[key]        
        sorted_value_timestamps = sorted(value_timestamps, key=lambda x: x[1], reverse=True)
        for i in sorted_value_timestamps:
            if i[1] <= timestamp:
                return i[0]
        return ""
