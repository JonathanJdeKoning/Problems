class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        start = 1
        idx = 0
        out = [0]*num_people
        while True:
            if candies - start < 0:
                start = candies
                out[idx] += start
                return out

            out[idx] += start
            candies -= start
            start += 1
            idx += 1
            if idx == num_people: idx = 0

