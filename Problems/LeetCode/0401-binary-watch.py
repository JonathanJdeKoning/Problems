class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        d = defaultdict(list)
        for hour in range(12):
            hBits = bin(hour).count("1")
            for minute in range(60):
                mBits = bin(minute).count("1")
                d[hBits+mBits].append(f"{hour}:{str(minute).zfill(2)}")
        return d[turnedOn] 

