class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        maxlen = 1
        currlen = 1
        curr = nums[0]
        lennums = [curr]
        maxnums = [curr]
        for i in nums[1:]:
            if i == curr + 1:
                currlen += 1
                lennums.append(i)
                if currlen > maxlen:
                    maxlen = currlen
                    maxnums = lennums
            else:
                break
            curr = i
        tot = sum(maxnums)
        while True:
            if tot in nums:
                tot += 1
            else:
                return tot
                break

