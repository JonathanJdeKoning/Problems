class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mp = defaultdict(int)
        mx = 0
        for s, e in intervals:
            mp[s] += 1
            mp[e] -= 1
        keys = sorted(mp.keys())
        curr = 0
        for k in keys:
            curr += mp[k]
            mx = max(curr, mx)
        return mx
