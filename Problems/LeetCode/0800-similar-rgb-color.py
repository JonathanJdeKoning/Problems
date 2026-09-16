class Solution:
    def similarRGB(self, color: str) -> str:
        p = ["AA", "BB", "CC", "DD", "EE", "FF", "00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]

        minDist = inf
        best = None
        a = int(color[1:3], 16)
        b = int(color[3:5], 16)
        c = int(color[5:7], 16)
        x = min(p, key=lambda i:(int(i, 16) - a)**2)
        y = min(p, key=lambda i:(int(i, 16) - b)**2)
        z = min(p, key=lambda i:(int(i, 16) - c)**2)

        return f"#{x}{y}{z}".lower()
