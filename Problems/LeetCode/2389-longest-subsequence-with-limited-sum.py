class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = [0]* len(queries)

        for i, q in enumerate(queries):
            count = 0
            summa = 0
            for num in nums:
                summa += num
                count += 1
                if summa <= q:
                    ans[i] = count
                else:
                    break
        return ans            
