class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        f_ = defaultdict(int)
        t_ = defaultdict(int)
        for n, f, t in trips:
            f_[f] += n
            t_[t] += n
        c = 0
        for i in range(1001):
            if i in t_:
                if c >= t_[i]:
                    c -= t_[i]
                else:
                    return False
            if i in f_:
                if f_[i] + c <= capacity:
                    c += f_[i]
                else: return False            

        return True