class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = []
        bits = defaultdict(deque)
        for i, num in enumerate(nums):
            tmp = num
            pos = 0
            while tmp:
                if tmp & 1:
                    bits[pos].append(i)
                tmp >>= 1
                pos += 1

        for i in range(len(nums)):
            furthest = i
            for pos in bits:
                furthest = max(furthest, bits[pos][0])
            ans.append((furthest - i) + 1)

            toodles = []
            for pos in bits:
                if bits[pos][0] == i:
                    bits[pos].popleft()
                if not bits[pos]:
                    toodles.append(pos)
            for pos in toodles:
                del bits[pos]

        return ans
