class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        for s, x in items:
            mp[s].append(x)
        ans = []

        for k,v in mp.items():
            
            ans.append([k, sum(sorted(v)[-5:]) // 5])

        return sorted(ans)