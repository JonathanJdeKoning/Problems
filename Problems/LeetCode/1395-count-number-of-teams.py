class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for j in range(1, len(rating) - 1):
            leftLess = 0
            leftMore = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                else:
                    leftMore += 1

            rightLess = 0
            rightMore = 0
            for k in range(j+1, len(rating)):
                if rating[k] < rating[j]:
                    rightLess += 1
                else:
                    rightMore += 1

            ans += leftLess * rightMore
            ans += leftMore * rightLess
        return ans