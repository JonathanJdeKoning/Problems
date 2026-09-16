class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], kk: int) -> List[int]:
        u = defaultdict(set)

        for user, time in logs:
            u[user].add(time)
        w = defaultdict(int)
        for k,v in u.items():
            w[len(v)] += 1
        ans = []
        for j in range(1,kk+1):
            ans.append(w.get(j,0))
        return ans
