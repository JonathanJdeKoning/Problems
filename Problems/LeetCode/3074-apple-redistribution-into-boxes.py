class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        count = 0
        while apples > 0:
            try:
                apples -= max(capacity)
            except: break
            capacity.remove(max(capacity))
            count += 1
        return count