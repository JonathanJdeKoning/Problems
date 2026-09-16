class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        start = round(sqrt(area))
        while True:
            test = area/start
            if test.is_integer():
                mn = min(test, start)
                mx = max(test, start)
                return [int(mx), int(mn)]
            start += 1