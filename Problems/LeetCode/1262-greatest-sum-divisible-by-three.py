class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        ones = []
        twos = []

        for num in nums:
            m = num % 3
            if m == 0: continue
            if m == 1:
                heappush(ones, -num)
                if len(ones) > 2:
                    heappop(ones)
            elif m == 2:
                heappush(twos, -num)
                if len(twos) > 2:
                    heappop(twos)

        ones = sorted([-x for x in ones], reverse=True)
        twos = sorted([-x for x in twos], reverse=True)

        M = total%3
        print(ones)
        print(twos)
        if M == 0: return total
        elif M == 1:
            if not ones and len(twos) < 2: return 0
            if ones and len(twos) < 2: return total-ones.pop()
            if not ones and len(twos) == 2: return total - sum(twos)
            return max(total-ones.pop(), total - sum(twos)) 
        elif M == 2:
            if not twos and len(ones) < 2: return 0
            if twos and len(ones) < 2: return total-twos.pop()
            if not twos and len(ones) == 2: return total - sum(ones)
            return max(total-twos.pop(), total - sum(ones)) 
        return 0