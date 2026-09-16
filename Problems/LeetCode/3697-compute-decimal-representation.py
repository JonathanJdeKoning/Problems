class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        place = 0
        ans = []
        while n:
            ans.append((n%10) * (10**place))
            place += 1
            n //= 10
        return [x for x in ans[::-1] if x]