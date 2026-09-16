class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0

        aIndices, bIndices, cIndices = [], [], []

        for i, char in enumerate(s):
            if char not in "abc": continue
            [aIndices,bIndices,cIndices][ord(char)-97].append(i)

        for left in range(len(s)):
            nextA = bisect_left(aIndices, left)
            nextB = bisect_left(bIndices, left)
            nextC = bisect_left(cIndices, left)

            if nextA == len(aIndices): continue
            if nextB == len(bIndices): continue
            if nextC == len(cIndices): continue

            lastGood = max(aIndices[nextA],bIndices[nextB],cIndices[nextC])
            ans += (N - lastGood)
        return ans