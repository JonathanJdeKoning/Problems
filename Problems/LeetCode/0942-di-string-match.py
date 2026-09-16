class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = s.count("D")
        out = [start]
        mn = start
        mx = start
        for c in s:
            if c == "I":
                out.append(mx+1)
                mx += 1
            else:
                out.append(mn-1)
                mn -= 1
        return out