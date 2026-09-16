class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = -math.inf
        for word in strs:
            if word.isdigit():
                mx = max(int(word), mx)
            else:
                mx = max(len(word), mx)
        return mx
