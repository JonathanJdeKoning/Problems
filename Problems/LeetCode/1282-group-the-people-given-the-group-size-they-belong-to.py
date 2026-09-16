class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp = defaultdict(list)
        ans = []
        for i, c in enumerate(groupSizes):
            mp[c].append(i)
            if len(mp[c]) == c:
                ans.append(mp[c])
                mp[c] = []
        return ans