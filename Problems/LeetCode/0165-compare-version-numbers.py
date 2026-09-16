class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = []
        v2 = []

        for chunk in version1.split("."):
            v1.append(int(chunk))
        for chunk in version2.split("."):
            v2.append(int(chunk))
        
        n = len(v1)
        m = len(v2)
        for i in range(min(n, m)):
            one = v1[i]
            two = v2[i]

            if one > two: return 1
            elif two > one: return -1

        if n == m: return 0
        if n > m:
            ntot = sum(v1[i+1:])
            if ntot > 0:
                return 1
            else: return 0

        else:
            mtot = sum(v2[i+1:])
            if mtot > 0:
                return -1
            else: return 0
