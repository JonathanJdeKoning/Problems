class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peeps = zip(names, heights)
        speep = sorted(peeps, key=lambda x:x[1], reverse=True)
        return [x[0] for x in speep]