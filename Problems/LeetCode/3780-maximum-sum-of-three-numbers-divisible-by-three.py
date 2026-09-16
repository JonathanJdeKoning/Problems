class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mods = [[],[],[]]
        for num in nums:
            mods[num%3].append(num)
        for i in range(3):
            mods[i] = sorted(mods[i])

        poss = []
        if len(mods[0]) >= 3:
            poss.append(sum(mods[0][-3:]))
        if len(mods[1]) >= 3:
            poss.append(sum(mods[1][-3:]))
        if len(mods[2]) >= 3:
            poss.append(sum(mods[2][-3:]))
        if mods[0] and mods[1] and mods[2]:
            poss.append(sum(row[-1] for row in mods))
        if poss: return max(poss)
        return 0 