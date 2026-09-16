from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        idx = bisect_left(self.d[key],timestamp,key=lambda x: x[0])
        if idx == len(self.d[key]) or self.d[key][idx][0] != timestamp: idx -= 1

        if idx == -1: return ""
        return self.d[key][idx][1]
       
           
