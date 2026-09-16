class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first]
        x = first
        for num in encoded:
            out.append(x^num)
            x = x^num
        return out