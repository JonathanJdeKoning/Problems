class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        total = 0

        for i in range(len(isConnected)):
            if i not in seen:
                stack = [i]
                total += 1
                while stack:
                    curr = stack.pop()
                    if curr in seen:continue
                    seen.add(curr)

                    for j in range(len(isConnected)):
                        if isConnected[curr][j] and j not in seen:
                            stack.append(j)
        return total



