class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue

            while stack and temp > stack[-1][0]:
                idx = stack.pop()[1]
                temperatures[idx] = i - idx
            stack.append((temp, i))

        for t, i in stack:
            temperatures[i] = 0
        return temperatures



            