class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = [colors[-1]] + colors + [colors[0]]
        total = 0 
        for i in range(1, len(colors)-1):
            if colors[i] != colors[i-1] and colors[i] != colors[i+1]:
                total += 1
        return total