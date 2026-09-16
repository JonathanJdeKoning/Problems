class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for word in dictionary:
                if len([x for x,y in zip(q,word) if x!=y])<=2:
                    ans.append(q)
                    break
        return ans