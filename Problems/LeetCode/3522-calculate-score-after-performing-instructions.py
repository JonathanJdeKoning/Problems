class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        total = 0
        i = 0
        seen = set()
        while True:
            if i not in range(0, len(instructions)):
                break
            if i in seen: break

            ins = instructions[i]
            seen.add(i)
            if ins == "add":
                total += values[i]
                i += 1
            else:
                i += values[i]
        return total