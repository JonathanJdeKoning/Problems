class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []

        for num in range(1,n+1):
            if num in target:
                out.append("Push")
                target.remove(num)
                if len(target) == 0: return out
            else:
                out.append("Push")
                out.append("Pop")
        return out
