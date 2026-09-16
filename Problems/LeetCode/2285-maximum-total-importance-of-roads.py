class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        total = 0
        freq = defaultdict(int)
        for a, b in roads:
            freq[a] += 1
            freq[b] += 1
        look = {}
        val = n

        for k, v in sorted(dict(freq).items(), key=lambda x:x[1], reverse = True):
            look[k] = val
            val -= 1

        for a, b in roads:
            total += look[a]
            total += look[b]           

        return total
