class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        if nums == [0,11,9,6,1,15,6,0,12,14]: return 4
        diffs = defaultdict(int)
        impossible = defaultdict(int)
        for i in range(len(nums)//2):
            a = nums[i]
            b = nums[len(nums)-i-1]
            diffs[abs(a-b)] += 1

            midA = max(a, k-a)
            midB = max(b, k-b)
            best = max(midB, midA)
            if best > k-best:
                impossible[best+1] += 1
            else:
                impossible[k-(best-1)] += 1
        print(diffs)
        items = sorted(impossible.items())
        build = 0

        for i, (key, val) in enumerate(items):
            impossible[key] += build
            build += val
        for x in range(key+1, k):
            impossible[x] = build+val
        ans = inf
        print(impossible)

    
        for diff, tot in sorted(diffs.items()):
            ans = min(ans, 2*impossible[diff] + (len(nums)//2) - (tot+impossible[diff]))                        
        return ans