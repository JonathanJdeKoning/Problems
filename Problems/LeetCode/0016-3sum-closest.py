class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        pairs = set()

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                pair = nums[i] + nums[j]
                pairs.add((pair, i,j))
        pairs = sorted(list(pairs))
        #print(pairs)
        ans = inf
        bestDist = inf
        for i, num in enumerate(nums):
            
            complement = target - num
            closest = bisect_left(pairs,complement,key=lambda x: x[0])

            if closest == len(pairs): closest -= 1
            
            if i not in pairs[closest][1:]:
                dist = abs(target - (num + pairs[closest][0]))
                if dist < bestDist:
                    bestDist = dist
                    ans = num + pairs[closest][0]
            
            l = closest-1
            r = closest+1
            
            while l > 0           and i in pairs[l][1:]: l -= 1
            while r < len(nums)-1 and i in pairs[r][1:]: r += 1

            if l >= 0 and i not in pairs[l][1:]:
                dist = abs(target - (num + pairs[l][0]))
                if dist < bestDist:
                    bestDist = dist
                    ans = num + pairs[l][0]

            if r < len(nums) and i not in pairs[r][1:]:
                dist = abs(target - (num + pairs[r][0]))
                if dist < bestDist:
                    bestDist = dist
                    ans = num + pairs[r][0]

        return ans
