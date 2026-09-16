class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        nums = list(map(lambda x: list(str(x)), nums))
        seen = set()
        other = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start = i+1):
                if (i,j) in seen: continue
                if a == b and len(a) == 1:
                    ans += 1
                    seen.add((i,j))
                    other.append((a,b))
                    continue
                for k, c in enumerate(a):
                    if (i,j) in seen: continue

                    for l, d in enumerate(a[k:], start = k):
                        if (i,j) in seen: continue

                        a[k] = d
                        a[l] = c

                        if int("".join(a)) == int("".join(b)):
                            ans += 1
                            seen.add((i,j))
                            other.append((a,b))
                        a[k] = c
                        a[l] = d

                if (i,j) in seen:continue
                for m, e in enumerate(b):
                    if (i,j) in seen: continue

                    for n, f in enumerate(b[m:], start = m):
                        if (i,j) in seen: continue
                        b[m] = f
                        b[n] = e

                        if int("".join(a)) == int("".join(b)):
                            ans += 1
                            seen.add((i,j))
                        b[m] = e
                        b[n] = f

        return ans


                
